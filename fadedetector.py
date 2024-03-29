__author__ = 'Kyle Long'
import cv2
import cv
import numpy as np


# Advanced Scene Detection Parameters
INTENSITY_THRESHOLD = 25  # Pixel intensity threshold (0-255)
MINIMUM_PERCENT     = 95   # The minimum amount of pixels allowed to be below threshold.
BLOCK_SIZE          = 32    # Number of rows to sum per iteration.


def main():

    capfile = #file name here in single quotes
    cap = cv2.VideoCapture()
    cap.open(capfile)

    if not cap.isOpened():
        print "Fatal error - could not open video %s." % capfile
        return
    else:
        print "Parsing video %s..." % capfile

    # Do stuff with cap here.

    width  = cap.get(cv.CV_CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv.CV_CAP_PROP_FRAME_HEIGHT)
    print "Video Resolution: %d x %d" % (width, height)

    # Allow the threshold to be passed as an optional, second argument to the script.
    threshold = 50

    print "Detecting scenes with threshold = %d" % threshold
    print "Min. pixels under threshold = %d %%" % MINIMUM_PERCENT
    print "Block/row size = %d" % BLOCK_SIZE
    print ""

    min_percent = MINIMUM_PERCENT / 100.0
    num_rows    = BLOCK_SIZE
    last_amt    = 0     # Number of pixel values above threshold in last frame.
    start_time  = cv2.getTickCount()  # Used for statistics after loop.

    while True:
        # Get next frame from video.
        (rv, im) = cap.read()
        if not rv:   # im is a valid image if and only if rv is true
            break

        # Compute # of pixel values and minimum amount to trigger fade.
        num_pixel_vals = float(im.shape[0] * im.shape[1] * im.shape[2])
        min_pixels     = int(num_pixel_vals * (1.0 - min_percent))

        # Loop through frame block-by-block, updating current sum.
        frame_amt = 0
        curr_row  = 0
        while curr_row < im.shape[0]:
            # Add # of pixel values in current block above the threshold.
            frame_amt += np.sum(
                im[curr_row : curr_row + num_rows,:,:] > threshold )
            if frame_amt > min_pixels:  # We can avoid checking the rest of the
                break                   # frame since we crossed the boundary.
            curr_row += num_rows

        # Detect fade in from set threshold.
        if frame_amt >= min_pixels and last_amt < min_pixels:
            print "Detected fade in at %dms (frame %d)." % (
                cap.get(cv2.cv.CV_CAP_PROP_POS_MSEC),
                cap.get(cv2.cv.CV_CAP_PROP_POS_FRAMES) )

        # Detect fade out to set threshold.
        elif frame_amt < min_pixels and last_amt >= min_pixels:
            print "Detected fade out at %dms (frame %d)." % (
                cap.get(cv2.cv.CV_CAP_PROP_POS_MSEC),
                cap.get(cv2.cv.CV_CAP_PROP_POS_FRAMES) )

        last_amt = frame_amt      # Store current mean to compare in next iteration.

    # Get # of frames in video based on the position of the last frame we read.
    frame_count = cap.get(cv2.cv.CV_CAP_PROP_POS_FRAMES)
    # Compute runtime and average framerate
    total_runtime = float(cv2.getTickCount() - start_time) / cv2.getTickFrequency()
    avg_framerate = float(frame_count) / total_runtime

    print "Read %d frames from video in %4.2f seconds (avg. %4.1f FPS)." % (
        frame_count, total_runtime, avg_framerate)

    cap.release()


if __name__ == "__main__":
    main()




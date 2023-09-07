# Description: Main script for the Raspberry Pi
import logging
import datetime
import picamera

from time import sleep
from io import BytesIO

def main():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s — %(name)s — [%(levelname)s]: %(message)s",
                        handlers=[
                            logging.StreamHandler(),  # For terminal output
                            logging.FileHandler('logfile.log')  # For log file
                        ])
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # Declare all variables that will be used in main() try block
    # Camera object, used to take pictures, if an exception occurs, this will be closed,
    # so it should be declared outside the try block
    camera = None
    logger.info("Declared [camera] reference in {ref_id}".format(ref_id=id(camera)))
    image_1 = None
    logger.info("Declared [image_1] reference in {ref_id}".format(ref_id=id(image_1)))
    image_2 = None
    logger.info("Declared [image_2] reference in {ref_id}".format(ref_id=id(image_2)))

    try:
        logger.info("Starting camera...")
        image_1 = open('test_1.jpg', 'wb')
        logger.info("Checking [image_1] reference in {ref_id}".format(ref_id=id(image_1)))
        image_2 = open('test_2.jpg', 'wb')
        logger.info("Checking [image_2] reference in {ref_id}".format(ref_id=id(image_2)))
        my_stream = BytesIO()
        camera = picamera.PiCamera()
        logger.info("Checking [camera] reference in {ref_id}".format(ref_id=id(camera)))
        camera.start_preview()
        # Camera warm-up time
        logger.info("Capturing image: 1")
        camera.capture(image_1)
        logger.info("Saved image: 1")
        sleep(10)
        # camera.capture(my_stream, 'jpeg')
        logger.info("Capturing image: 2")
        camera.capture(image_2)
        logger.info("Saved image: 2")
        camera.stop_preview()
        camera.close()
    except:
        logger.exception("Exception occurred", exc_info=True)
    finally:
        if camera:
            camera.close()
        logger.info("Camera closed")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

import logging
import datetime
import picamera

from time import sleep
from io import BytesIO

from modules.camera import CameraV1


def main():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s — %(name)s — [%(levelname)s]: %(message)s",
                        handlers=[
                            logging.StreamHandler(),  # For terminal output
                            logging.FileHandler('logfile.log')  # For log file
                        ])
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logging.info("Starting camera...")
    camera = None
    try:
        camera = CameraV1()
        # camera.list_camera()  # Dang bi bug
        camera.exposure('off')
        camera.iso(100)
        camera.start_for_capturing()
        camera.capture('test_1.jpg')
        sleep(10)
        camera.capture('test_2.jpg')
        camera.close()
    except:
        logger.exception("Exception occurred", exc_info=True)
    finally:
        if camera:
            camera.close()
        logger.info("Camera closed")


if __name__ == '__main__':
    main()
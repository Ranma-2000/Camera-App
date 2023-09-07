import picamera
import logging

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s — %(name)s — [%(levelname)s]: %(message)s",
                    handlers=[
                        logging.StreamHandler(),  # For terminal output
                        logging.FileHandler('logfile.log')  # For log file
                    ])


class CameraV1:

    def __init__(self):
        self.logger = logging.getLogger('CameraV1')
        self.logger.setLevel(logging.INFO)
        self.logger.info("Creating camera instance")
        self.camera = picamera.PiCamera(
            resolution=(1280, 720),
            framerate=30,
            sensor_mode=3
        )
        self.IS_START_FOR_CAPTURING = False

    def capture(self, filename):
        # Write try block here to catch exception while capturing image
        try:
            if self.IS_START_FOR_CAPTURING:
                self.logger.info("Capturing image: {filename}".format(filename=filename))
                self.camera.capture(open(filename, 'wb'))
                return 0
            else:
                raise Exception("Camera is not started for capturing")
        except:
            self.logger.debug('Capturing image failed')
            self.logger.exception("Exception occurred", exc_info=True)
            return -1

    def list_camera(self):
        available_camera = self.camera.list_cameras()
        if available_camera:
            for camera in available_camera:
                self.logger.info("Available camera: {camera}".format(camera=camera))
        else:
            self.logger.info("No camera available")

    def close(self):
        self.logger.info("Closing camera")
        if self.IS_START_FOR_CAPTURING:
            self.camera.stop_preview()
        self.camera.close()

    def exposure(self, value):
        self.logger.info("Setting exposure mode to: {value}".format(value=value))
        try:
            if value in ['off', 'auto']:
                self.camera.exposure_mode = value
                return 0
            else:
                raise ValueError("Invalid exposure mode")
        except ValueError:
            self.logger.exception("Exception occurred", exc_info=True)
            return -1

    def iso(self, value):
        self.logger.info("Setting ISO to: {value}".format(value=value))
        self.camera.iso = value

    def shutter_speed(self, value):
        self.logger.info("Setting shutter speed to: {value}".format(value=value))
        try:
            if value >= self.camera.framerate:
                self.camera.shutter_speed = value
                return 0
            else:
                raise ValueError("Shutter speed must be greater than framerate")
        except ValueError:
            self.logger.exception("Exception occurred", exc_info=True)
            return -1

    def framerate(self, value):
        self.logger.info("Setting framerate to: {value}".format(value=value))
        try:
            if isinstance(value, int) or isinstance(value, float):
                self.camera.framerate = value
                return 0
            else:
                raise ValueError("Invalid framerate value, in this app, framerate must be an integer or float")
        except ValueError:
            self.logger.exception("Exception occurred", exc_info=True)
            return -1

    def resolution(self, value):
        self.logger.info("Setting resolution to: {value}".format(value=value))
        try:
            if (isinstance(value, tuple) and len(value) == 2 and isinstance(value[0], int) and isinstance(value[1], int)
                    and value[0] > 0 and value[1] > 0) and (value[0] <= 2592 and value[1] <= 1944):
                self.camera.resolution = value
                return 0
            else:
                raise ValueError("Invalid resolution value, in this app, resolution must be a tuple, and meet some requirements")
        except ValueError:
            self.logger.exception("Exception occurred", exc_info=True)
            return -1

    def sensor_mode(self, value):
        self.logger.info("Setting sensor mode to: {value}".format(value=value))
        try:
            if isinstance(value, int) and value in [0, 1, 2, 3, 4, 5, 6, 7]:
                self.camera.sensor_mode = value
                return 0
            else:
                raise ValueError("Invalid sensor mode value, in this app, sensor mode must be an integer and in [0, 7]")
        except ValueError:
            self.logger.exception("Exception occurred", exc_info=True)
            return -1

    def start_for_capturing(self):
        self.logger.info("Starting camera for capturing")
        try:
            self.camera.start_preview()  # Should check system status while previewing
            self.IS_START_FOR_CAPTURING = True
            return 0
        except:
            self.logger.exception("Exception occurred", exc_info=True)
            self.IS_START_FOR_CAPTURING = False
            return -1

import logging
import unittest

from time import sleep

import programmingtheiot.common.ConfigConst as ConfigConst

from programmingtheiot.cda.emulated.PICGradeSensorEmulatorTask import (
    PICGradeSensorEmulatorTask,
)


class PICGradeEmulatorTaskTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        logging.basicConfig(
            format="%(asctime)s:%(module)s:%(levelname)s:%(message)s",
            level=logging.DEBUG,
        )
        logging.info("Testing PICGradeEmulatorTaskTest class")
        self.gradeEmuTask = PICGradeSensorEmulatorTask()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testReadEmulator(self):
        sd1 = self.gradeEmuTask.generateTelemetry()

        if sd1:
            self.assertEqual(sd1.getTypeID(), ConfigConst.GRADE_SENSOR_TYPE)
            logging.info("SensorData: %f - %s", sd1.getValue(), str(sd1))

            # wait 5 seconds
            sleep(5)
        else:
            logging.warning("FAIL: SensorData is None.")

        sd2 = self.gradeEmuTask.generateTelemetry()

        if sd2:
            self.assertEqual(sd2.getTypeID(), ConfigConst.GRADE_SENSOR_TYPE)
            logging.info("SensorData: %f - %s", sd2.getValue(), str(sd2))

            # wait 5 seconds
            sleep(5)
        else:
            logging.warning("FAIL: SensorData is None.")


if __name__ == "__main__":
    unittest.main()

import logging
import unittest

import programmingtheiot.common.ConfigConst as ConfigConst

from programmingtheiot.cda.sim.PICGradeSensorSimTask import PICGradeSensorSimTask


class PICGradeSensorSimTaskTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        logging.basicConfig(
            format="%(asctime)s:%(module)s:%(levelname)s:%(message)s",
            level=logging.DEBUG,
        )
        logging.info("Testing PICGradeSensorSimTask class...")
        self.gradeSimTask = PICGradeSensorSimTask()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGenerateTelemetry(self):
        sd = self.gradeSimTask.generateTelemetry()

        if sd:
            logging.info("SensorData: " + str(sd))
        else:
            logging.warning("SensorData is None.")

    # @unittest.skip("Ignore for now.")
    def testGetTelemetryValue(self):
        val = self.gradeSimTask.getTelemetryValue()
        logging.info("Grade data: %f", val)
        self.assertGreater(val, ConfigConst.DEFAULT_VAL)


if __name__ == "__main__":
    unittest.main()

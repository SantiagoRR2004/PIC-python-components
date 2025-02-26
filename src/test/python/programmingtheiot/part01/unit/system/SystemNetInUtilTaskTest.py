#####
#
# This class is part of the Programming the Internet of Things
# project, and is available via the MIT License, which can be
# found in the LICENSE file at the top level of this repository.
#
# Copyright (c) 2020 by Andrew D. King
#

import logging
import unittest

from programmingtheiot.cda.system.SystemNetInUtilTask import SystemNetInUtilTask


class SystemNetInUtilTaskTest(unittest.TestCase):
    """
    This test case class contains very basic unit tests for
    SystemNetInUtilTask. It should not be considered complete,
    but serve as a starting point for the student implementing
    additional functionality within their Programming the IoT
    environment.
    """

    @classmethod
    def setUpClass(self):
        logging.basicConfig(
            format="%(asctime)s:%(module)s:%(levelname)s:%(message)s",
            level=logging.DEBUG,
        )
        logging.info("Testing SystemNetInUtilTask class...")
        self.netInUtilTask = SystemNetInUtilTask()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGetTelemetryValue(self):
        val = self.netInUtilTask.getTelemetryValue()

        self.assertGreaterEqual(val, 0.0)
        logging.info("Number of bytes received: %s", str(val))


if __name__ == "__main__":
    unittest.main()

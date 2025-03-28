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

import programmingtheiot.common.ConfigConst as ConfigConst

from programmingtheiot.cda.system.ActuatorAdapterManager import ActuatorAdapterManager
from programmingtheiot.common.DefaultDataMessageListener import (
    DefaultDataMessageListener,
)

from programmingtheiot.data.ActuatorData import ActuatorData


class ActuatorAdapterManagerTest(unittest.TestCase):
    """
    This test case class contains very basic unit tests for
    ActuatorSimAdapterManager. It should not be considered complete,
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
        logging.info("Testing ActuatorAdapterManager class...")

        self.defaultMsgListener = DefaultDataMessageListener()
        self.actuatorAdapterMgr = ActuatorAdapterManager()
        self.actuatorAdapterMgr.setDataMessageListener(self.defaultMsgListener)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testHumidifierSimulation(self):
        ad = ActuatorData(typeID=ConfigConst.HUMIDIFIER_ACTUATOR_TYPE)
        ad.setValue(50.0)

        ad.setCommand(ConfigConst.COMMAND_ON)
        self.actuatorAdapterMgr.sendActuatorCommand(ad)

        ad.setCommand(ConfigConst.COMMAND_OFF)
        self.actuatorAdapterMgr.sendActuatorCommand(ad)

    def testHvacSimulation(self):
        ad = ActuatorData(typeID=ConfigConst.HVAC_ACTUATOR_TYPE)
        ad.setValue(22.5)

        ad.setCommand(ConfigConst.COMMAND_ON)
        self.actuatorAdapterMgr.sendActuatorCommand(ad)

        ad.setCommand(ConfigConst.COMMAND_OFF)
        self.actuatorAdapterMgr.sendActuatorCommand(ad)


if __name__ == "__main__":
    unittest.main()

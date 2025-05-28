import logging
import webbrowser

import programmingtheiot.common.ConfigConst as ConfigConst

from programmingtheiot.cda.sim.BaseActuatorSimTask import BaseActuatorSimTask


class PICTestEmulatorTask(BaseActuatorSimTask):
    """
    We want it to open some PIC tests when activated.
    """

    def __init__(self):

        super(PICTestEmulatorTask, self).__init__(
            name=ConfigConst.TEST_ACTUATOR_NAME,
            typeID=ConfigConst.TEST_ACTUATOR_TYPE,
            simpleName="PICTest",
        )

    def _activateActuator(
        self, val: float = ConfigConst.DEFAULT_VAL, stateData: str = None
    ) -> int:

        # Temporary url
        webbrowser.open("https://github.com/programming-the-iot/python-components")
        return 0

    def _deactivateActuator(
        self, val: float = ConfigConst.DEFAULT_VAL, stateData: str = None
    ) -> int:

        logging.info(self.getSimpleName() + " told not to create tests.")
        return 0

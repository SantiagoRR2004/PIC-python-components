import logging

import programmingtheiot.common.ConfigConst as ConfigConst

from programmingtheiot.cda.sim.BaseActuatorSimTask import BaseActuatorSimTask

import subprocess
import sys
import os


if not os.path.exists("TestCreator"):
    logging.info("TestCreator directory not found. Running TestCreator script first.")
    subprocess.run(["bash", "downloadTestCreator.sh"], check=True)

sys.path.append(os.path.abspath("."))
sys.path.append(os.path.abspath("TestCreator"))

from TestCreator.UTILS import exam


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

        # Change to the TestCreator directory
        os.chdir(os.path.abspath("TestCreator"))

        exam.examGenerator(
            folderPath=os.path.abspath("PIC"),
            numberOfExams=int(val),
            numberOfQuestions=30,
        )

        # Change back to the original directory
        os.chdir(os.path.abspath(".."))

        return 0

    def _deactivateActuator(
        self, val: float = ConfigConst.DEFAULT_VAL, stateData: str = None
    ) -> int:

        logging.info(self.getSimpleName() + " told not to create tests.")
        return 0

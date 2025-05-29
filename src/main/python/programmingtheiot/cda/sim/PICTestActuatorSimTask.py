import programmingtheiot.common.ConfigConst as ConfigConst
from programmingtheiot.cda.sim.BaseActuatorSimTask import BaseActuatorSimTask


class PICTestActuatorSimTask(BaseActuatorSimTask):

    def __init__(self):
        super(PICTestActuatorSimTask, self).__init__(
            name=ConfigConst.TEST_ACTUATOR_NAME,
            typeID=ConfigConst.TEST_ACTUATOR_TYPE,
            simpleName="PICTest",
        )

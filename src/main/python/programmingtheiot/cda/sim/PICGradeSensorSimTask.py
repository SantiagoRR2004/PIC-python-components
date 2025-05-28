import programmingtheiot.common.ConfigConst as ConfigConst

from programmingtheiot.cda.sim.BaseSensorSimTask import BaseSensorSimTask
from programmingtheiot.cda.sim.SensorDataGenerator import SensorDataGenerator


class PICGradeSensorSimTask(BaseSensorSimTask):

    def __init__(self, dataSet=None):
        super(PICGradeSensorSimTask, self).__init__(
            name=ConfigConst.GRADE_SENSOR_NAME,
            typeID=ConfigConst.GRADE_SENSOR_TYPE,
            dataSet=dataSet,
            minVal=SensorDataGenerator.LOW_NORMAL_GRADE,
            maxVal=SensorDataGenerator.HI_NORMAL_GRADE,
        )

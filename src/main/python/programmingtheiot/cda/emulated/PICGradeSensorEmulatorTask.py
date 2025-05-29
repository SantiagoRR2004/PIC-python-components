import random

from programmingtheiot.data.SensorData import SensorData

import programmingtheiot.common.ConfigConst as ConfigConst
from programmingtheiot.common.ConfigUtil import ConfigUtil

from programmingtheiot.cda.sim.BaseSensorSimTask import BaseSensorSimTask


class PICGradeSensorEmulatorTask(BaseSensorSimTask):
    """
    SenseHAT doesn't doesn't have something like making
    grades so I don't use it
    """

    def __init__(self, dataSet=None):
        super(PICGradeSensorEmulatorTask, self).__init__(
            name=ConfigConst.GRADE_SENSOR_NAME,
            typeID=ConfigConst.GRADE_SENSOR_TYPE,
            minVal=ConfigUtil().getFloat(
                section=ConfigConst.CONSTRAINED_DEVICE,
                key=ConfigConst.GRADE_SIM_FLOOR_KEY,
                defaultVal=0,
            ),
            maxVal=ConfigUtil().getFloat(
                section=ConfigConst.CONSTRAINED_DEVICE,
                key=ConfigConst.GRADE_SIM_CEILING_KEY,
                defaultVal=10,
            ),
        )

    def generateTelemetry(self) -> SensorData:
        sensorData = SensorData(name=self.getName(), typeID=self.getTypeID())

        # The exam has 30 questions so they always answer half of them
        answeredQuestions = 15 + random.randint(0, 15)

        # Choose the ones that were incorrect
        incorrectQuestions = random.randint(0, answeredQuestions)

        # The number of questions that count
        questions = answeredQuestions - incorrectQuestions - incorrectQuestions // 4

        # The grade is the number of questions divided by 3
        grade = questions / 3

        sensorData.setValue(grade)
        self.latestSensorData = sensorData

        return sensorData

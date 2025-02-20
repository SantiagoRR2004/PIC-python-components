#####
#
# This class is part of the Programming the Internet of Things project.
#
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

import programmingtheiot.common.ConfigConst as ConfigConst

from programmingtheiot.data.BaseIotData import BaseIotData


class SystemPerformanceData(BaseIotData):
    """
    Shell representation of class for student implementation.

    """

    DEFAULT_VAL = 0.0

    def __init__(self, d=None):
        super(SystemPerformanceData, self).__init__(
            name=ConfigConst.SYSTEM_PERF_MSG, typeID=ConfigConst.SYSTEM_PERF_TYPE, d=d
        )

        self.cpuUtil = ConfigConst.DEFAULT_VAL
        self.memUtil = ConfigConst.DEFAULT_VAL

    def __str__(self):
        return "SystemPerformanceData [cpuUtil={}, memUtil={}]".format(
            self.cpuUtil, self.memUtil
        )

    def getCpuUtilization(self) -> float:
        return self.cpuUtil

    def getDiskUtilization(self):
        pass

    def getMemoryUtilization(self) -> float:
        return self.memUtil

    def setCpuUtilization(self, cpuUtil: float) -> None:
        self.cpuUtil = cpuUtil
        self.updateTimeStamp()

    def setDiskUtilization(self, diskUtil):
        pass

    def setMemoryUtilization(self, memUtil: float) -> None:
        self.memUtil = memUtil
        self.updateTimeStamp()

    def _handleUpdateData(self, data) -> None:
        if data and isinstance(data, SystemPerformanceData):
            self.cpuUtil = data.getCpuUtilization()
            self.memUtil = data.getMemoryUtilization()

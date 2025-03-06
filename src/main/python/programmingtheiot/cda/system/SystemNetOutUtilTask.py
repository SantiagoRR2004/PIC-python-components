#####
#
# This class is part of the Programming the Internet of Things project.
#
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

import logging
import psutil

import programmingtheiot.common.ConfigConst as ConfigConst

from programmingtheiot.cda.system.BaseSystemUtilTask import BaseSystemUtilTask


class SystemNetOutUtilTask(BaseSystemUtilTask):
    """
    Shell representation of class for student implementation.

    """

    def __init__(self):
        super(SystemNetOutUtilTask, self).__init__(
            name=ConfigConst.NETOUT_UTIL_NAME, typeID=ConfigConst.NETOUT_UTIL_TYPE
        )
        self.last = psutil.net_io_counters().bytes_recv

    def getTelemetryValue(self) -> int:
        """
        Get the telemetry value

        We need to get the amount of bytes sent
        since the last call
        """
        new = psutil.net_io_counters().bytes_recv
        diff = new - self.last
        self.last = new
        return diff

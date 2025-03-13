import redis
import logging

import programmingtheiot.common.ConfigConst as ConfigConst
from programmingtheiot.common.ConfigUtil import ConfigUtil

from programmingtheiot.common.ResourceNameEnum import ResourceNameEnum
from programmingtheiot.data.SensorData import SensorData


class RedisPersistenceAdapter:
    def __init__(self):
        self.configUtil = ConfigUtil()
        self.host = self.configUtil.getProperty(
            ConfigConst.DATA_GATEWAY_SERVICE, ConfigConst.HOST_KEY
        )
        self.port = self.configUtil.getProperty(
            ConfigConst.DATA_GATEWAY_SERVICE, ConfigConst.PORT_KEY
        )

        self.client = None  # Redis client instance

        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

        self.logger.info(
            f"RedisPersistenceAdapter initialized with host: {self.host}, port: {self.port}"
        )

    def connectClient(self) -> bool:
        if self.client and self.client.ping():
            self.logger.warning("Redis client is already connected.")
            return True

        try:
            self.client = redis.Redis(host=self.host, port=self.port)

            if self.client.ping():
                self.logger.info("Connected to Redis successfully.")
                return True

            else:
                self.logger.error("Failed to connect to Redis.")
                return False

        except Exception as e:
            self.logger.error(f"Error connecting to Redis: {e}")
            return False

    def disconnectClient(self) -> bool:
        if not self.client or not self.client.ping():
            self.logger.warning("Redis client is already disconnected.")
            return True

        try:
            self.client.close()
            self.client = None
            self.logger.info("Disconnected from Redis successfully.")
            return True

        except Exception as e:
            self.logger.error(f"Error disconnecting from Redis: {e}")
            return False

    def storeData(self, resource: ResourceNameEnum, data: SensorData) -> bool:
        if not self.client or not self.client.ping():
            self.logger.error("Failed to connect to Redis.")
            return False

        try:
            topic = f"{resource}"

            # Store in Redis
            self.client.set(topic, str(data.getValue()))

            self.logger.info(f"Stored sensor data in Redis under topic: {topic}")
            return True

        except Exception as e:
            self.logger.error(f"Error storing sensor data in Redis: {e}")
            return False

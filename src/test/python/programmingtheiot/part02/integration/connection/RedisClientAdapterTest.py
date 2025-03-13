import logging
import unittest

from programmingtheiot.cda.connection.RedisPersistenceAdapter import (
    RedisPersistenceAdapter,
)

from programmingtheiot.common.ResourceNameEnum import ResourceNameEnum
from programmingtheiot.data.SensorData import SensorData


class RedisClientAdapterTest(unittest.TestCase):

    DEFAULT_NAME = "SensorDataFooBar"
    VALUE = 10.0

    @classmethod
    def setUpClass(self):
        logging.basicConfig(
            format="%(asctime)s:%(module)s:%(levelname)s:%(message)s",
            level=logging.DEBUG,
        )
        logging.info("Running RedisClientAdapterTest test cases...")

        self.redisAdapter = RedisPersistenceAdapter()

    def setUp(self):
        logging.info("================================================")
        logging.info("DataIntegrationTest test execution...")
        logging.info("================================================")

    def tearDown(self):
        pass

    def testConnectClient(self):
        """
        Test Redis client connection.
        """
        result = self.redisAdapter.connectClient()
        self.assertTrue(result)

    def testDisconnectClient(self):
        """
        Test Redis client disconnection.
        """
        self.redisAdapter.connectClient()  # Ensure it's connected first
        result = self.redisAdapter.disconnectClient()
        self.assertTrue(result)

    def testStoreSensorData(self):
        """
        Test storing sensor data in Redis.
        """
        self.redisAdapter.connectClient()  # Ensure it's connected

        # Create a sample SensorData instance
        sensor_data = SensorData()
        sensor_data.setName(self.DEFAULT_NAME)
        sensor_data.setValue(self.VALUE)

        resource = ResourceNameEnum.CDA_SENSOR_MSG_RESOURCE

        result = self.redisAdapter.storeData(resource, sensor_data)
        self.assertTrue(result)

        # Verify data was stored
        stored_value = self.redisAdapter.client.get(str(resource))
        # The value returned will be in bytes
        self.assertEqual(stored_value, str(sensor_data.getValue()).encode("utf-8"))

        self.redisAdapter.disconnectClient()


if __name__ == "__main__":
    unittest.main()

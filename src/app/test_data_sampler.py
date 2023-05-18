"""This module tests Data Sampler using unittest."""
import unittest
from data_sampler import DataSampler
from helpers import EntriesData

class TestApp(unittest.TestCase):
    """Test classes and methods using UnitTest."""
    
    def setUp(self):
        self.sampler = DataSampler()
    
    def tearDown(self):
        pass
    
    def test_data_sampler(self):
        sample = self.sampler.get_sample(20)
        self.assertEqual(20, len(sample))
        self.assertIsInstance(sample[0], EntriesData)


# if __name__ == '__main__':
#     unittest.main()

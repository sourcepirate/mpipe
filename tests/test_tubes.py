import tests.context
import unittest
from time import sleep
from mpipe.TubeP import TubeP
from mpipe.TubeQ import TubeQ


class TestUnorderedPipe(unittest.TestCase):
    """Test the un ordered tube

       Module to be tested : TubeP

    """

    def setUp(self):
        self.pipe = TubeP()

    def test_tube_put_and_get(self):
        self.pipe.put(10)
        self.assertEquals(10, self.pipe.get())

    def test_tube_put_and_get_with_timeout(self):
        sleep(0.04)
        self.pipe.put(10)
        self.assertTrue(self.pipe.get(0.04)[0])
        self.assertFalse(self.pipe.get(0.04)[0])


class TestOrderedPipe(unittest.TestCase):
    """Test the OrderedTube

       Module to be tested: TubeQ
    """

    def setUp(self):
        self.pipe = TubeQ()

    def test_tube_put_and_get(self):
        self.pipe.put(10)
        self.assertEquals(10, self.pipe.get())

    def test_tube_put_and_get_with_timeout(self):
        sleep(0.04)
        self.pipe.put(10)
        self.assertTrue(self.pipe.get(0.04)[0])
        self.assertFalse(self.pipe.get(0.04)[0])

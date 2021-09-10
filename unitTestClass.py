import unittest
from arrayElements import groupArrayElements
class unitTestClass(unittest.TestCase):
    def test_groupArrayElements(self):
        self.assertEqual(groupArrayElements([1,3,4,5],2),[[1,3],[4,5]])
    def test_exceptions(self):
        self.assertEqual(groupArrayElements([1,3,4,5],0),"'n' should be greater than zero")
        self.assertEqual(groupArrayElements([],9),"'arrayElements' should not be a empty list")
if __name__ == '__main__':
    unittest.main()
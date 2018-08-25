import unittest
from square_mod import square


class SquareTest(unittest.TestCase):
    def setUp(self):
        print("setUp - started!")
        self.values = ((0, 0), (1, 1), (2, 4), (3, 9), (4, 16))
        print("setUp - finished!")

    def testCalc(self):
        for val, res in self.values:
            self.assertEqual(square(val), res)

    def tearDown(self):
        print("setDown - started!")
        del self.values
        print("tearDown - finished!")


if __name__ == "__main__":
    unittest.main()

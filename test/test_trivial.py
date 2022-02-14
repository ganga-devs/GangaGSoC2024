import unittest
import copy


class TestTrivial(unittest.TestCase):

    def test_reference(self):
        a = [1]
        b = a
        a[0] = 2
        self.assertEqual(b[0], 2)

    def test_copy(self):
        a = [1]
        b = copy.deepcopy(a)
        a[0] = 2
        self.assertFalse(b[0] == 2)


if __name__ == '__main__':
    unittest.main()

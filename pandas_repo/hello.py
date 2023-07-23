def add_two_nums(num1, num2):
  return num1 + num2 

# Path: test_hello.py
import unittest
from hello import add_two_nums

class TestAddTwoNums(unittest.TestCase):
  def test_add_two_nums(self):
    self.assertEqual(add_two_nums(3, 5), 8)
    self.assertEqual(add_two_nums(-1, 1), 0)
    self.assertEqual(add_two_nums(-1, -1), -2)
    self.assertEqual(add_two_nums(5, 5), 10)


if __name__ == '__main__':
  unittest.main()
# Path: hello.py
# def add_two_nums(num1, num2):
#   return num1 + num2
# # Path: test_hello.py
# import unittest
# from hello import add_two_nums
# class TestAddTwoNums(unittest.TestCase):
#   def test_add_two_nums(self):

  


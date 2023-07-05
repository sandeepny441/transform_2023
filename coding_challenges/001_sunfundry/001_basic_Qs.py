# Python Program to Check if a Number is Odd or Even
def is_even(given_num):
    return True if given_num%2 ==0 else False
print(is_even(23))

# Python Program to Check Whether a Number is Positive or Negative
def is_positive(given_num):
    return given_num >= 0 
print(is_positive(23))

#Python Program to Print All Odd Numbers in a Range
def all_odd_nums(given_range):
    res_list = []
    for num in range(0, given_range+1):
        if num%2 !=0:
            res_list.append((num))
print(all_odd_nums(22))


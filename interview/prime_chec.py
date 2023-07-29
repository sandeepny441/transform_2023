# def draw_pyramid_pattern(given_num):
#   row_number = 1
#   column_number = 1 
#   while row_number < 4:
#     while column_number < 6:
#       if row_number + column_number 

# AABAA: 4 
# ABABA: 4, 6
# BABAB: 

# program for pyramid pattern of stars, equilateral triangle
# Path: pyramid_pattern.py
def draw_pyramid_pattern(given_num):
  row_number = 1
  column_number = 1
  while row_number <= given_num:
    while column_number <= given_num:
      if row_number + column_number >= given_num + 1:
        print("*", end="")
      else:
        print(" ", end="")
      column_number += 1
    print()
    row_number += 1
    column_number = 1
  

draw_pyramid_pattern(4)
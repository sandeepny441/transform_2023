# Palindrome Program in Python
def is_palindrome(given_num):
    given_num_str = str(given_num)
    if given_num_str == given_num_str[::-1]:
        return True 
    return False
print(is_palindrome(121))

# Palindrome Program in Python
def is_palindrome(given_num):
    given_num_str = str(given_num)
    if given_num_str == given_num_str[::-1]:
        return f"{given_num} is Palindrome"
    return f"{given_num} is Not palindrome"
print(is_palindrome(121))

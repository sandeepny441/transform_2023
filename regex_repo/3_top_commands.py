import re

# . Matches any character except newline
print(re.search('a.b', 'acb'))  # Matches
print(re.search('a.b', 'a\nb'))  # Does not match

# * Matches zero or more of the preceding element
print(re.search('a*', 'aaab'))  # Matches

# + Matches one or more of the preceding element
print(re.search('a+', 'aaab'))  # Matches
print(re.search('a+', 'b'))  # Does not match

# ? Makes the preceding element optional
print(re.search('a?', 'b'))  # Matches

# {n} Matches exactly n repetitions of the preceding element
print(re.search('a{2}', 'aa'))  # Matches

# {n,m} Matches between n and m repetitions of the preceding element
print(re.search('a{2,3}', 'aaa'))  # Matches

# [abc] Matches any character enclosed in the square brackets
print(re.search('[abc]', 'b'))  # Matches
print(re.search('[abc]', 'd'))  # Does not match

# [^abc] Matches any character NOT enclosed in the square brackets
print(re.search('[^abc]', 'd'))  # Matches
print(re.search('[^abc]', 'a'))  # Does not match

# ^ Matches the start of the string
print(re.search('^abc', 'abcdef'))  # Matches
print(re.search('^abc', 'abcdefabc'))  # Matches
print(re.search('^abc', 'abcdefabcdef'))  # Matches



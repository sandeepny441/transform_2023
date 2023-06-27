#match 
import re
print(re.match('a', 'abc'))  # Matches
print(re.match('a', 'bac'))  # Does not match


# findall
import re
print(re.findall('a', 'abcabc'))  # Returns ['a', 'a']


'''
Regular Expression: Regular expressions (regex or regexp) are patterns used to match and manipulate text. 
They are widely used in programming languages like Python, JavaScript, and Perl for searching, replacing, and validating textual data. 
A regular expression is a sequence of characters that define a search pattern. It consists of a combination of special characters and normal characters, which are used to form a search pattern. 
The regular expression engine matches this pattern against text and provides various operations like search, replace, and splitting of text.
'''

import re

mystr = '''Tata Limited
Dr. David Landsman, executive director
18, Grosvernor place
London, SW1X 7HSc
Phone: +44 (20) 7235 8281
Fax: +44 (20) 7235 8727
Email: tata@tata.co.uk
Website: www.europe.tat.com
Directions: View map

Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: +1 (703) 243 9787
Fax: +1 (703) 243 9791 
66-66
455-4545
Email: northamerica@tata.com
Website: www.northamerica.tata.com
Directions: View map fass
harry bhai lekin
bahut hi badia aadmi haiaiin'''

# Meta characters are special characters that have a unique meaning in regular expressions. 
# These characters are used to create complex patterns that can match various types of text. 
# Some of the commonly used meta characters in regular expressions are:
# . (dot) - matches any single character except newline.
# * (asterisk) - matches zero or more occurrences of the previous character.
# + (plus) - matches one or more occurrences of the previous character.
# ? (question mark) - matches zero or one occurrence of the previous character.
# ^ (caret) - matches the beginning of the string.
# $ (dollar) - matches the end of the string.
# [] (square brackets) - matches any one of the characters inside the brackets.
# | (pipe) - matches either the expression before or after the pipe.
# () (parentheses) - creates a group and captures the matched text.
# \ (backslash) - escapes the following character and matches it literally.


# In Python, a raw string is a string literal that is prefixed with an 'r' or 'R'. 
# When a string is declared as a raw string, any escape sequences in the string are ignored, and the backslash character is treated as a regular character. 
# This is particularly useful when working with regular expressions, file paths, and other strings that may contain backslashes. 
# For example, to create a regular expression pattern that matches a backslash character, you would need to use a raw string to avoid escaping the backslash itself.
# Base rule of using a regular expression, we always use  raw strings


# to find a string in the mystr string

patt = re.compile(r'fass') # we want to search fass in the mystr
matches = patt.finditer(mystr)
for match in matches:
    print(match) # this return the span i.e. from which character number the fass start and at which character it ends i.e.
    print(mystr[449:453])
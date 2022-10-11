'''
F-Strings & String Formatting
'''

# String formating

import math
me = 'Harry'
strng = "this is %s" % me
print(strng)

# or it can be done as
a1 = 'code'
str1 = 'this is %s %s' % (me, a1)
print(str1)


# but if we have to insert many variables inside a string than this method is not convenient.
# to overcome this we can actually use string formating as

str2 = 'this is {0} {1}'
b = str2.format(me, a1)
print(b)
# in this way we can also change the location or formating as
str3 = 'this is {1} {0}'
b2 = str3.format(me, a1)
print(b2)

# this string formating method is good but still readability is not good in this program.
# So to further improve this program f-string is used
# f in f-string stands for fast

a2 = f'this is {me} {a1}'  # this is how f-string is used
print(a2)

# we can also use the module function also as


a3 = f'this is {me} {a1} {math.cos(90)}'
print(a3)

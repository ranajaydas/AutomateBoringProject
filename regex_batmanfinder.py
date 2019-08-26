import re

""" 1. Finds any Batman related objects in a string """

print('\n1.\n')
raw_text = "Oh no! The Batmobile lost a wheel just now! What will Batman do now?"
bat_regex = re.compile(r'Bat(man|mobile|phone|copter|belt)')      # define the pattern to look for
mo = bat_regex.findall(raw_text)                                   # mo is short for match objects
print(mo.group())


""" 2. Another example """
print('\n2.\n')

bat_regex2 = re.compile(r'Bat(wo)?man')                           # ? represents an optional pattern

mo1 = bat_regex2.search('The Adventures of Batwoman')
print(mo1.group())

mo2 = bat_regex2.search('The Adventures of Batman')
print(mo2.group())


""" 3. Another Example """
print('\n3.\n')

bat_regex3 = re.compile(r'Bat(wo)*man')                           # * matches zero or more. Replace with + for 1 or more

mo1 = bat_regex3.search('The Adventures of Batwoman')
print(mo1.group())

mo2 = bat_regex3.search('The Adventures of Batman')
print(mo2.group())

mo3 = bat_regex3.search('The Adventures of Batwowowowoman')
print(mo3.group())


"""
Shorthand character class Represents
\d      Any numeric digit from 0 to 9.
\D      Any character that is not a numeric digit from 0 to 9.
\w      Any letter, numeric digit, or the underscore character.
        (Think of this as matching “word” characters.)
\W      Any character that is not a letter, numeric digit, or the
        underscore character.
\s      Any space, tab, or newline character. (Think of this as
        matching “space” characters.)
\S      Any character that is not a space, tab, or newline.
"""

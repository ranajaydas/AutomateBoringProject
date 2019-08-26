import re

raw_text = 'My name is Ranajay Das. My phone number is +65 96648194. My other cell number is +65 97776555'

""" Find a phone number without using any grouping """
print(' Without grouping '.center(30, '='))

phone_regex1 = re.compile(r'\+\d{2} \d{8}')       # can also add () around the \d to create groups
mo1 = phone_regex1.search(raw_text)               # mo is short for match objects

if mo1:
    print('Phone number found:', mo1.group())
else:
    print('Number not found.')


""" Find a phone number with grouping """
print(' With grouping '.center(30, '='))

phone_regex2 = re.compile(r'(\+\d{2}) (\d{8})')      # can also add () around the \d to create groups
mo2 = phone_regex2.search(raw_text)                  # mo is short for match objects

if mo2:
    print('Phone number found:', mo2.group())
    print('Country code:', mo2.group(1))
    print('Phone number:', mo2.group(2))
else:
    print('Number not found.')


""" Finds multiple phone numbers """
print(' Multiple Phone Numbers '.center(30, '='))

mo3 = phone_regex1.findall(raw_text)                  # findall will create a list

if mo3:
    print('Phone number(s) found:', mo3)

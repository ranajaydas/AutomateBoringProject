""" An extremely boring program that finds the phone numbers and email addresses in the clipboard
Here's some text to copy to the clipboard:

Hello, my name is Ranajay Das. My email ID is ranajay@gmail.com. This extremely
boring program is my way of breaking into the world of coding. If you don't like it
you can send your complaints to +65 96648194 where they will be promptly ignored. In fact
I am so bored with Regexes that I could just call my ex at +65 81980444! My god, I can't
believe I still remember that!

Anyway, you can probably email someone at fuckuapalooza@fuckles.com.sg to register your
many complaints as I'm sure you'll have them or you can just call (+972) 89991281 for any
further enquiries. BYE!

"""


import re
import pyperclip

phone_regex = re.compile(r'''(
                             (\+\d+|\(\+\d+\))?         # Country code which may be enclosed in () 
                             (\s|-|\.)?                 # Separator
                             (\d+)                      # Phone number
                             )''', re.VERBOSE)

email_regex = re.compile(r'''(
                             [a-zA-Z0-9._%+-]+          # Username 
                             @                          # @
                             [a-zA-Z0-9.-]+             # domain name
                             (\.[a-zA-Z]{2,4})          # dot something
                             )''', re.VERBOSE)

raw_text = str(pyperclip.paste())                       # pastes the clipboard into raw_text
matches = []


for groups in phone_regex.findall(raw_text):
    matches.append(groups[0])

for groups in email_regex.findall(raw_text):
    matches.append(groups[0])

if len(matches):
    print('\nEmails & phone numbers found and copied to clipboard:\n')
    print('\n'.join(matches))
    pyperclip.copy('\n'.join(matches))
else:
    print('No email addresses or phone numbers found.')

#! python3
"""This is an insecure password locker program"""

import sys
import pyperclip

passwords = {'email': '#FW@@22k21dkmw',
             'blog': 'choot099@@31w',
             'luggage': '8900'}

if len(sys.argv) < 2:
    print('Usage: python os_pw.py <accountname> - copy account password')      # Type in pw <account name> in Windows Run
    print(sys.argv)
    sys.exit()

account = sys.argv[1]       # first command line arg is the account name

if account in passwords:
    pyperclip.copy(passwords[account])
    print('Password for {} copied to clipboard'.format(account))
else:
    print('There is no account named {}, you little shite'.format(account))

import re

robocop_regex = re.compile(r'robocop', re.IGNORECASE)       # can also use re.I instead of re.IGNORECASE

print(robocop_regex.search('RoboCop is part man, part machine, all cop!').group())
print(robocop_regex.search('I want to be like robocop when I grow up!').group())
print(robocop_regex.search('I used to steal the controller while playing ROBOCOP!').group())
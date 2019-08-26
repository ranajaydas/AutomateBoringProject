import re

phrase1 = 'Agent Smith and Agent Anderson are currently fucking each other while Agent Fishburne watches in horror.'
print(phrase1, '\n')

names_regex = re.compile(r'Agent \w+')
print(names_regex.sub('CENSORED', phrase1))

agent_names_regex = re.compile(r'Agent (\w)\w*')
print(agent_names_regex.sub(r'Herr \1****', phrase1))     # \1 matches the first group found i.e. (\w)

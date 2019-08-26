import re

print("""== 1. The . wildcard ==""")

phrase1 = 'The rains in Spain are mainly in the plains'
wild_regex1 = re.compile(r'.ain')
print(wild_regex1.findall(phrase1))

wild_regex2 = re.compile(r'.ains')
print(wild_regex2.findall(phrase1))


print("""== 2. The * wildcard ==""")

phrase2 = 'First Name: Ranajay Last Name: Das'
name_regex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = name_regex.search(phrase2)
print(mo.group(1))
print(mo.group(2))


print(r"""== 3. Include \n in the search ==""")

phrase3 = 'Serve the public trust.\nProtect the innocent.\nUphold the law.'
noNewlineRegex = re.compile('.*')
print(noNewlineRegex.search(phrase3).group())

newlineRegex = re.compile('.*', re.DOTALL)
print(newlineRegex.search(phrase3).group())

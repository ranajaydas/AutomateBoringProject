import re

phrase = 'RoboCop eats baby food. BABY FOOD!'

vowel_regex = re.compile(r'[aeiouAEIOU]')                        # can also use hyphen like [a-zA-Z0-9]
print(vowel_regex.findall(phrase))

consonant_regex = re.compile(r'[^aeiouAEIOU ]')                 # ^ for exclude, ' ' for space (can also use \s)
print(consonant_regex.findall(phrase))

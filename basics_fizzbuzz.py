"""Simple program to do the fizzbuzz test."""

# The most simple way to do it
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('fizzbuzz')
    elif i % 3 == 0:
        print('fizz')
    elif i % 5 == 0:
        print('buzz')
    else:
        print(i)

print()
# Slightly better way
for i in range(1, 101):
    output = ''
    if not i % 3:
        output += 'fizz'
    if not i % 5:
        output += 'buzz'
    if not output:
        output = i
    print(output)

"""The Slightly Less Reader Friendly Poem of Life."""

cycles = 5         # The number of cycles you have to repeat

end_words = ['flame', 'breath', 'embrace', 'thread\n', 'milk', 'love', 'kiss', 'shove\n',
             'hook', 'song', 'rhyme', 'dance', 'time\n']

hook_words = {'darkness\n': 'Shine\n',
              'sorrow\n': 'Cry\n',
              'song\n': 'Sing\n',
              'sky\n': 'Fly\n'}

SUFFIXES = {1: 'st', 2: 'nd', 3: 'rd'}


# Adds a suffix to the cycle you're on
def cycle_with_suffix(num):
    if num == cycles:
        return 'last'
    elif 10 <= num % 100 <= 20:
        suffix = 'th'
    else:
        suffix = SUFFIXES.get(num % 10, 'th')
    return str(num) + suffix


# The hook of the poem
def the_hook(num):
    hook = ''
    article = ''

    if num < cycles:
        start = 'If life is '
    else:
        start = 'Life is THE '

    for k, v in hook_words.items():
        if k == 'song\n' and num < cycles:
            article = 'a '
        elif k == 'sky\n' and num < cycles:
            article = 'the '
        hook += start + article + k + v

    return hook


# The poem
print('The Poem of Life\n')
for cycle in range(1, cycles+1):
    for word in end_words:
        if word == 'hook':
            print('Such is life\n\n{}'.format(the_hook(cycle)))
        elif word == 'time\n':
            print('Your {0} {1}'.format(cycle_with_suffix(cycle), word))
        else:
            print('The {0} {1}'.format(cycle_with_suffix(cycle), word))

    if cycle == cycles-1:
        print('Learn this poem by heart\nFor its lines, they repeat\n')

print('Such is the poem of life\nRecite it well')

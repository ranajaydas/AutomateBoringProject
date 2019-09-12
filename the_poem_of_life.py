"""The Poem of Life."""

cycles = 5         # The number of cycles you have to repeat


# Adds a suffix to all the cycles
def cycle_with_suffix(num):
    if str(num).endswith('1') and not str(num).endswith('11'):
        suff = 'st'
    elif str(num).endswith('2') and not str(num).endswith('12'):
        suff = 'nd'
    elif str(num).endswith('3') and not str(num).endswith('13'):
        suff = 'rd'
    else:
        suff = 'th'
    return str(num) + suff


# The hook of the poem
def the_hook(num):
    if num < cycles:
        hook = """
If life is darkness\nShine
If life is sorrow\nCry
If life is a song\nSing
If life is the sky\nFly"""
    else:
        hook = """
Life is THE darkness\nShine
Life is THE sorrow\nCry
Life is THE song\nSing
Life is THE sky\nFly"""

    return hook


# The poem
print('The Poem of Life')
for cycle in range(1, cycles+1):
    if cycle == cycles:
        the_0 = 'last'
    else:
        the_0 = cycle_with_suffix(cycle)
    
    print("""
The {0} flame\nThe {0} breath\nThe {0} embrace\nThe {0} thread\n
The {0} milk\nThe {0} love\nThe {0} kiss\nThe {0} shove\n
Such is life
{1}

The {0} song\nThe {0} rhyme\nThe {0} dance\nYour {0} time
""".format(the_0, the_hook(cycle)))

    if cycle == cycles-1:
        print('Learn this poem by heart\nFor its lines, they repeat')

print('Such is the poem of life\nRecite it well')

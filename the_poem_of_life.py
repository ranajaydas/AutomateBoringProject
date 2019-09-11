"""The Poem of Life"""

cycles = 15         # The number of cycles you have to repeat


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
        hook = """If life is darkness
    Shine
    If life is sorrow
    Cry
    If life is a song
    Sing
    If life is the sky
    Fly"""

    else:
        hook = """Life is THE darkness
    Shine
    Life is THE sorrow
    Cry
    Life is THE song
    Sing
    Life is THE sky
    Fly"""

    return hook


# The poem
print('The Poem of Life')
for cycle in range(1, cycles+1):
    
    if cycle == cycles:
        the_0 = 'last'
    else:
        the_0 = cycle_with_suffix(cycle)
    
    print("""
    The {0} flame
    The {0} breath
    The {0} embrace
    The {0} thread
    
    The {0} milk
    The {0} love
    The {0} kiss
    The {0} shove
    
    Such is life
    
    {1}

    The {0} song
    The {0} rhyme
    The {0} dance
    Your {0} time
    """.format(the_0, the_hook(cycle)))

    if cycle == cycles-1:
        print("""    Learn this poem by heart
    For its lines, they repeat""")


print("""    Such is the poem of life
    Recite it well""")

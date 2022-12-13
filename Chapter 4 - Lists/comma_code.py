"""Comma Code"""

stuff = ['apples', 'bananas', 'tofu', 'cats']


def joiner(list_input):
    """Returns comma separated string with 'and' inserted before last item"""
    joined = ''
    for item in list_input[:-1]:
        joined += item + ', '
    joined += 'and ' + list_input[-1]
    return joined


print(joiner(stuff))

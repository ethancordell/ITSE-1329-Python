def not_string(string):
    if string[0:3] == 'not':
        return string
    else:
        add = 'not ' + string
        return add
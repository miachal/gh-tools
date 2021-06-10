"""
    Simple AoB tool.

    > python -V
    Python 3.4.1
	
"""

def cmp(a, b):
    """
        a = 'aa bb cc dd 00 11'
        b = 'ab cc dc dd 00 61'
        ret 'a? ?? ?c dd 00 ?1'
    """

    out = []
    if a == '':
        return b

    range_len = (len(b), len(a))[len(a) <= len(b)]
    out += (('?', a[i])[a[i] == b[i]] for i in range(0, range_len))

    return out

def make_aob(list):
    """
        get list ( readlines() ) from file
        ret string aob
    """
    aob = ''
    for line in list:
        line = line.strip()
        if line != '' and not line.startswith(';'):
            aob = cmp(aob, line)
    return ''.join(aob)


if __name__ == '__main__':
	
    # Open file
    file = open('in.txt', 'r+')

    # Make AoB
    aob = make_aob(file.readlines())

    # Save result
    file.write('\n\n; AoB\n')
    file.write(aob)

    # Close file
    file.close()

    print("Done.")



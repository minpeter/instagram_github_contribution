def fileopen(filename):
    msg = """"""

    f = open(filename, 'r')
    lines = f.readlines()
    for line in lines:
        msg += str(line)
    f.close()

    return msg



def convertAtoI(string):

    if not string:
        return
    if not string[1:].isnumeric():
        return
    sign, res = 1, 0
    j = 0
    if string[0] == '-':
        sign = -1
        j = 1

    for i in range(j, len(string)):
        res = res*10+ord(string[i])-ord('0')
    res = sign*res
    return res


if __name__ == "__main__":
    print(convertAtoI('737839'))

def product(s, last):
    if last:
        s = s.split('*')
        cur = int(s[0].replace('m', '-'))
        for i in range(1, len(s)):
            cur *= int(s[i].replace('m', '-'))
        return cur

    s = s.replace('-', ' - ')
    s = s.replace('+', ' + ')
    s = s.split()
    for i in range(len(s)):
        if '*' in s[i]:
            temp = s[i].split('*')

            res = int(temp[0].replace('m', '-')) * int(temp[1].replace('m', '-'))
            if res<0:
                s[i] = 'm' + str(abs(res))
            else:
                s[i] = str(res)
    s = ''.join(s)
    return s

def add(s, last):
    if last:
        s = s.split('+')
        cur = int(s[0].replace('m', '-'))
        for i in range(1, len(s)):
            cur += int(s[i].replace('m', '-'))
        return cur

    s = s.replace('*', ' * ')
    s = s.replace('-', ' - ')
    s = s.split()
    for i in range(len(s)):
        if '+' in s[i]:
            temp = s[i].split('+')

            res = int(temp[0].replace('m', '-')) + int(temp[1].replace('m', '-'))
            if res<0:

                s[i] = 'm' + str(abs(res))
            else:
                s[i] = str(res)
    s = ''.join(s)

    return s

def minus(s,last):
    if last:
        s = list(map(int, s.split('-')))
        cur = s[0]
        for i in range(1, len(s)):
            cur -= s[i]
        return cur

    else:
        s = s.replace('*', ' * ')
        s = s.replace('+', ' + ')
        s = s.split()
        for i in range(len(s)):
            if '-' in s[i]:
                temp = list(map(int, s[i].split('-')))
                res = temp[0] - temp[1]
                if res < 0:
                    s[i] = 'm' + str(abs(res))
                else:
                    s[i] = str(res)
        s = ''.join(s)
    return s
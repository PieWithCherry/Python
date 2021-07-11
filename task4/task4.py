from sys import argv

str1, str2 = argv[1], argv[2]


def checkString(str1, str2):
    count = 0
    out = ''
    for o in str2:
        if o != '*':
            out += o
    if str1 == out:
        return 'OK'
    for i in range(len(str1)):
        if len(str2) == 0 and len(str1) != 0:
            return 'KO'
        if str1[i] == str2[i]:
            count += 1
            if count == len(str2) and len(str2) != len(str1):
                return 'KO'
            continue
        elif str1[i] != str2[i]:
            if str2[i] == '*':
                if len(str2) - 1 == count:
                    return 'OK'
                for j in range(count, len(str2)):
                    if str2[j] == '*':
                        continue
                    else:
                        if str2[-1:j - 1:-1] == str1[-1:(len(str1) - len(str2[-1:j - 1:-1])) - 1:-1]:
                            return 'OK'
                        else:
                            return 'KO'
            else:
                return 'KO'
    if bool(str2[count::]) == True:
        for k in range(count, len(str2)):
            if str2[k] == '*':
                continue
            else:
                return 'KO'
    return "OK"


if __name__ == '__main__':
    print(checkString(str1, str2))

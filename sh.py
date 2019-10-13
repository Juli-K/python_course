def count(s):
    res = 0
    alphav = "abcdefghijklmnopqrstuvwxz"
    for i in alphav:
        res = s.count(i)
        print(i, res)
    return res

def shifr(s, key):
    new = ""
    Alpha = {
        0 : 'a',
        1 : 'b',
        2 : 'c',
        3 : 'd',
        4 : 'e',
        5 : 'f',
        6 : 'g',
        7 : 'h',
        8 : 'i',
        9 : 'j',
        10 : 'k',
        11 : 'l',
        12 : 'm',
        13 : 'n',
        14 : 'o',
        15 : 'p',
        16 : 'q',
        17 : 'r',
        18 : 's',
        19 : 't',
        20 : 'u',
        21 : 'v',
        22 : 'w',
        23 : 'x',
        24 : 'y',
        25 : 'z',
    }
    for i in s:
        new += Alpha[(ord(i) - ord('a') + key) % 26]
    return new

def deshifr(s, key):
    out = ""
    Alpha = {
        0 : 'a',
        1 : 'b',
        2 : 'c',
        3 : 'd',
        4 : 'e',
        5 : 'f',
        6 : 'g',
        7 : 'h',
        8 : 'i',
        9 : 'j',
        10 : 'k',
        11 : 'l',
        12 : 'm',
        13 : 'n',
        14 : 'o',
        15 : 'p',
        16 : 'q',
        17 : 'r',
        18 : 's',
        19 : 't',
        20 : 'u',
        21 : 'v',
        22 : 'w',
        23 : 'x',
        24 : 'y',
        25 : 'z',
    }
    for i in s:
        out += Alpha[(ord(i) - ord('a') - key) % 26]
    return out


string = input()
key = int(input())
string = string.lower()
newstring = shifr(string, key)
print(newstring)
res = count(newstring)
d = input()
key = int(input())
out = deshifr(d, key)
print(out)

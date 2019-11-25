import sys
import struct
import random
import argparse
def Key():
    f = open(args.out, 'wb');
    num = random.sample(range(0, 256), 256)
    index = 0
    while index < 256:
        f.write(struct.pack('>B', num[index]))
        index += 1
    f.close()

def Enc():
    f_key = open(args.key[0], 'rb')
    f_ip = open(args.key[1], 'r')
    f_op = open('output.bin', 'wb')
    alf = f_key.read()
    for line in f_ip:
        for index in line:
            f_op.write(alf[ord(index) - 1])
    f_key.close()
    f_ip.close()
    f_op.close()

def Dec():
    f_key = open(args.key[0], 'rb')
    f_ip = open(args.key[1], 'rb')
    f_op = open('output.txt', 'w')
    alf = f_key.read()
    byte = f_ip.read(1)
    while byte != '':
        tmp = alf.index(byte) + 1
        f_op.write(chr(tmp))
        byte = f_ip.read(1)
    f_key.close()
    f_ip.close()
    f_op.close()

#import numpy as np

def Model():
    #count = np.zeros(256, dtype=np.int)#[0 for j in range(256)]
    count = [0 for j in range(256)]
    size = 0
    for fname in args.file:
        f = open(fname ,'r')
        for line in f:
            for index in line:
                count[ord(index)] +=1
                size += 1
        f.close()
            # count += np.array([line.count(chr(c)) for c in range(256)], dtype = np.int)
    #  count = [count[i]/size for i in 256]
    i = 0
    res = open('model.bin', 'wb')
    while i < 256:
        count[i] /= float(size)
        res.write(struct.pack('>f', count[i]))
        i += 1
    res.close()


def Broke():
    count1 = [0 for j in range(256)]
    size = 0
    f = open(args.file[0], 'r')
    for line in f:
        for index in line:
            count1[ord(index)] +=1
            size += 1
    f.close()
    i = 0
    while i < 256:
        count1[i] /= float(size)
        i += 1
    Count1 = {i: count1[i] for i in range(256)}
    m = open(args.file[1], 'rb')
    Count2 = {i: m.read(sys.float_info) for i in range(256)}
    print Count2
    m.close()

parser = argparse.ArgumentParser(description = "Modes:\n1)key\n2)enc\n3)dec\n")
parser.add_argument("mode", type = str)
parser.add_argument("-o", "--out", "--out-file")
parser.add_argument("-k", "--key", type = str, default = 'sec.key', help = 'file name with key', nargs = 2)
parser.add_argument("file", type = str, help = 'name file for make model', nargs = '*')
args = parser.parse_args()
if args.mode == 'key':
    Key()
elif args.mode == 'enc':
    Enc()
elif args.mode == 'dec':
    Dec()
elif args.mode == 'makemodel':
    Model()
elif args.mode == 'broke':
    Broke()

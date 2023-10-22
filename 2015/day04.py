import os 
import hashlib
from itertools import count

here = os.path.dirname(__file__)

def read_data(fname):
    here = os.path.dirname(__file__)
    with open(os.path.join(here,fname),'r') as f:
        return f.read() 


def part1(input):

    for postfix in (str(i) for i in count(1)):
        hash = hashlib.md5((input + postfix).encode('utf-8')).hexdigest()
        if hash[:5] == '00000':
            print(postfix)
            return 

def part2(input):

    for postfix in (str(i) for i in count(1)):
        hash = hashlib.md5((input + postfix).encode('utf-8')).hexdigest()
        if hash[:6] == '000000':
            print(postfix)
            return 
        

input = read_data('day04.txt')
part1(input)
part2(input)

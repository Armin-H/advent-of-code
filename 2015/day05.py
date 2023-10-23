import os

def read_data(fname):
    here = os.path.dirname(__file__)
    with open(os.path.join(here,fname),'r') as f:
        return [s.strip() for s in f.readlines()]
    
def part1(input):
    nice_count = 0
    for s in input:
        naughty = False
        for bad in ['ab', 'cd', 'pq', 'xy']:
            if bad in s: 
                naughty = True 
        if naughty == True: 
            continue 
        
        if sum(map(s.count,'aeoiu')) <3: 
            continue
        else: 
            twice_in_a_row = False
            
            for i in range(0,len(s)-1,1):
                a,b = s[i:i+2]
                if a == b: 
                    
                    twice_in_a_row = True
            if twice_in_a_row == False:
                continue
        nice_count+=1
    print(nice_count)


def part2(input):
    # nice_count = 0
    # for s in input:     
    #     print(s)
    #     for i in range(0,len(s)-1,2):
    #         print(s[i:i+2])
input = read_data('day05.txt')
part1(input)
part2(input)
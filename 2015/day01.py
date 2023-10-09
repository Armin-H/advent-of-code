import os 

def read_data(fname):
    here = os.path.dirname(__file__)
    with open(os.path.join(here,fname)) as f :
        
        return f.read()
    
def part1(input):
    lvl =0
    for c in input:
        if c=='(':
            lvl+=1
        elif c==')':
            lvl-=1
        else:
            print(f'unkown char {c}')
            break
    return lvl

def part2(input):
    lvl = 0  
    for i,c in enumerate(input):
        
        if c=='(':
            lvl+=1
        elif c==')':
            lvl-=1
            if lvl == -1:
                return  i+1
            
        else:
            print(f'unkown char {c}')
            break
    raise Exception('didn\'t go to basement')

def combined(input):
    lvl = 0 
    pos = 0 
    first_time = True
    for i,c in enumerate(input):
        
        if c=='(':
            lvl+=1
        elif c == ')':
            lvl-=1
            if lvl ==-1 and first_time==True: 
                pos = i+1
                first_time = False

        else:
            raise Exception('unkown char')
    
    return lvl,pos

input = read_data('day01.txt')

p1ans = part1(input)
p2ans = part2(input)
print(combined(input))
print(p1ans,p2ans)
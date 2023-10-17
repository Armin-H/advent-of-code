import os 

def read_data(fname):
    here = os.path.dirname(__file__)
    with open(os.path.join(here,fname),'r') as f:
        return  f.read()
    
def part1(input):
    visit_seq = [(0,0)]
    for d in input:
        current_pos = visit_seq[-1]
        if d == '>':
            new_pos = (current_pos[0]+1,current_pos[1])
        elif d == '<':
            new_pos = (current_pos[0]-1,current_pos[1])
        elif d == '^':
            new_pos = (current_pos[0],current_pos[1]+1)
        elif d  == 'v':
            new_pos = (current_pos[0],current_pos[1]-1)
        else : 
            raise Exception(f'invalid char:{d}')
        visit_seq.append(new_pos)
    print(len(set(visit_seq)))


def part2(input):
    visited_seq_santa = [(0,0)]
    visited_seq_robo = [(0,0)]
    santa_turn  = True
    for d in input:
        seq  = visited_seq_santa if santa_turn else visited_seq_robo
        current_pos = seq[-1]
        if d == '>':
            new_pos = (current_pos[0]+1,current_pos[1])
        elif d == '<':
            new_pos = (current_pos[0]-1,current_pos[1])
        elif d == '^':
            new_pos = (current_pos[0],current_pos[1]+1)
        elif d  == 'v':
            new_pos = (current_pos[0],current_pos[1]-1)
        else : 
            raise Exception(f'invalid char:{d}')
        seq.append(new_pos)
        santa_turn = not santa_turn
    print(len(set(visited_seq_robo+visited_seq_santa)))

def combined(input,robo_active=True):
    visited_seq_santa = [(0,0)]
    visited_seq_robo = [(0,0)]
    santa_turn  = True
    for d in input:
        seq  = visited_seq_santa if santa_turn else visited_seq_robo
        current_pos = seq[-1]
        if d == '>':
            new_pos = (current_pos[0]+1,current_pos[1])
        elif d == '<':
            new_pos = (current_pos[0]-1,current_pos[1])
        elif d == '^':
            new_pos = (current_pos[0],current_pos[1]+1)
        elif d  == 'v':
            new_pos = (current_pos[0],current_pos[1]-1)
        else : 
            raise Exception(f'invalid char:{d}')
        seq.append(new_pos)
        if robo_active:
            santa_turn = not santa_turn
    
    print(len(set(visited_seq_robo+visited_seq_santa)))




input = read_data('day03.txt')
part1(input)
part2(input)
combined(input,robo_active=False)
combined(input,robo_active=True)
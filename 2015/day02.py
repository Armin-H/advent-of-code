import os

def read_data(fname):
    here = os.path.dirname(__file__)
    with open(os.path.join(here,fname),'r') as f:
        return f.readlines()

def part1(input):
    need = 0 
    for dims in input:
        l,w,h = map(int,dims.strip().split('x'))
        lw = l*w
        lh = l*h
        wh = w*h
        need += 2*lw + 2*lh + 2*wh + min(lw,lh,wh)
    print(need)

def part2(input):
    need = 0
    for dims in input:
        l,w,h = map(int,dims.strip().split('x'))
        need += sum(sorted((l,w,h))[:2])*2
        need += l*w*h
    print(need)

def combined(input):
    paper = 0
    ribbon = 0
    for dims in input: 
        l,w,h = map(int,dims.strip().split('x'))
        lw = l*w
        lh = l*h
        wh = w*h
        paper += 2*lw + 2*lh + 2*wh + min(lw,lh,wh)
        ribbon += sum(sorted((l,w,h))[:2])*2
        ribbon += l*w*h
    print(paper)
    print(ribbon)
input = read_data('day02.txt')
part1(input)
part2(input)
combined(input)
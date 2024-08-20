N, M = map(int, input().split())

group2mem = dict()
mem2group = dict()
for _ in range(N):
    group = input()
    group2mem[group] = []
    population = int(input())
    for _ in range(population):
        mem = input()
        group2mem[group].append(mem)
        mem2group[mem] = group
    group2mem[group].sort()

for _ in range(M):
    name = input()
    cmd = int(input())
    if cmd:
        print(mem2group[name])
    else:
        for itm in group2mem[name]:
            print(itm)
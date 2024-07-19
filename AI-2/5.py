import copy

###     moveGen START     ###
def moveGen(state):
    nbors=[] 
    for i in range(len(state)):
        if(len(state[i]) >= 1):
            for j in range(len(state)):
                if i!=j:
                    temp = copy.deepcopy(state)
                    top = temp[i].pop()
                    temp[j].append(top)
                    nbors.append(temp)
    return nbors
###     moveGen END    ###
    
###     goalTest START     ###
def goalTest(state, goal):
    if state==goal:
        return True
    else:
        return False
###     goalTest END     ###


###     HEURISTICS START     ###
#    First heuristic START
def oneadder(state1, state2):
    heu=0
    for m,i in enumerate(state1):
        for n,j in enumerate(i):
            for p,x in enumerate(state2):
                for q,y in enumerate(x):
                    if j == y:
                        if n == q and m==p:
                            heu+=1
    return -heu
#    First heuristic END

#    Second heuristic START
def leveladder(state1, state2):
    heu=0
    for m,i in enumerate(state1):
        for n,j in enumerate(i):
            for p,x in enumerate(state2):
                for q,y in enumerate(x):
                    if j == y:
                        if n == q and m==p:
                            heu+=(q+1)
    return -heu
#    Second heuristic END

#    Third heuristic START
def manhattan(state1, state2):
    heu=0
    for m,i in enumerate(state1):
        for n,j in enumerate(i):
            for p,x in enumerate(state2):
                for q,y in enumerate(x):
                    if j == y:
                        heu = heu + abs(m-p) + abs(n-q)
    return heu 
#    Third heuristic END
###     HEURISTICS END     ###




###     HILL CLIMBING START     ###
def hillClimbing(start, goal, heuristic):
    pathlen = 1
    curr = start
    explored = []
    explored.append(start)
    max = heuristic(start, goal)

    while not goalTest(curr, goal):
        nbors = moveGen(curr)
        check = False
        for v in nbors:
            if v not in explored:
                if heuristic(v, goal) <= max:
                    max = heuristic(v, goal)
                    curr = v
                    check = True
        explored.append(curr)
        pathlen+=1
        if not check:
            return pathlen, False, curr
    
    return pathlen, True, goal
###     HILL CLIMBING END     ###




temp = []
# For taking input from input.txt
inp_file = open("Sampleinput.txt")
for line in inp_file:
    m = len(line)-1
    line = line[0:m]
    temp.append(list(line))

# List for initial state
start = []
for i in range(3):
    start.append(temp[i])

# List for final state
goal = []
for i in range(4,7):
    goal.append(temp[i])

out_file = open('output.txt', 'w')
out_file.write('\n\n')
out_file.write('Analysis of Hill Climbing:-')

HM_pathlen, HM_status, final = hillClimbing(start, goal, manhattan)
out_file.write('\n\t(i)Manhattan:-')
out_file.write('\n\t\tStates explored = ')
out_file.write(str(HM_pathlen))
if HM_status:
    out_file.write('\n\t\tCompletion status = Reached GOAL state')
else:
    out_file.write('\n\t\tCompletion status = Cannot reach GOAL state')
out_file.write('\n\t\tFinal State = ')
out_file.write(str(final))

HO_pathlen, HO_status, final = hillClimbing(start, goal, oneadder)
out_file.write('\n\t(ii)One Adder:-')
out_file.write('\n\t\tStates explored = ')
out_file.write(str(HO_pathlen))
if HO_status:
    out_file.write('\n\t\tCompletion status = Reached GOAL state')
else:
    out_file.write('\n\t\tCompletion statu = Cannot reach GOAL state')
out_file.write('\n\t\tFinal State = ')
out_file.write(str(final))

HL_pathlen, HL_status, final = hillClimbing(start, goal, leveladder)
out_file.write('\n\t(iii)Level Adder:-')
out_file.write('\n\t\tStates explored = ')
out_file.write(str(HL_pathlen))
if HL_status:
    out_file.write('\n\t\tCompletion status = Reached GOAL state')
else:
    out_file.write('\n\t\tCompletion status = Cannot reach GOAL state')
out_file.write('\n\t\tFinal State = ')
out_file.write(str(final))
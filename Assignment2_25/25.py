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


###     SEARCH ALGORITHMS START     ###
from queue import PriorityQueue
###     BEST FIRST SEARCH START     ###
def BeFS(start, goal, heuristic):
    pathlen = 0
    heap = PriorityQueue()
    heap.put((heuristic(start, goal), start))
    explored = []
    explored.append(start)
    
    while heap:
        pathlen+=1
        temp = heap.get()
        state = temp[1]
        if goalTest(state, goal):
            return pathlen, True, goal 

        nbors = moveGen(state)
        for v in nbors:
            if v not in explored:
                heap.put((heuristic(v, goal), v))
                explored.append(v)

    return pathlen, False, goal
###     BEST FIRST SEARCH END     ###

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
###     SEARCH ALGORITHMS END     ###



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
out_file.write('2) Analysis of Hill Climbing:-')

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


"""
# For writing output.txt
out_file = open('output.txt', 'w')
out_file.write('1) Analysis of Best First Search:-')

BM_pathlen, BM_status, final = BeFS(start, goal, manhattan)
out_file.write('\n\t(i)Manhattan:-')
out_file.write('\n\t\tStates explored = ')
out_file.write(str(BM_pathlen))
if BM_status:
    out_file.write('\n\t\tCompletion status = Reached GOAL state')
else:
    out_file.write('\n\t\tCompletion status = Cannot reach GOAL state')
out_file.write('\n\t\tFinal State = ')
out_file.write(str(final))

BO_pathlen, BO_status, final = BeFS(start, goal, oneadder)
out_file.write('\n\t(ii)One Adder:-')
out_file.write('\n\t\tStates explored = ')
out_file.write(str(BO_pathlen))
if BO_status:
    out_file.write('\n\t\tCompletion status = Reached GOAL state')
else:
    out_file.write('\n\t\tCompletion status = Cannot reach GOAL state')
out_file.write('\n\t\tFinal State = ')
out_file.write(str(final))

BL_pathlen, BL_status, final = BeFS(start, goal, leveladder)
out_file.write('\n\t(iii)Level Adder:-')
out_file.write('\n\t\tStates explored = ')
out_file.write(str(BL_pathlen))
if BL_status:
    out_file.write('\n\t\tCompletion status = Reached GOAL state')
else:
    out_file.write('\n\t\tCompletion status = Cannot reach GOAL state')
out_file.write('\n\t\tFinal State = ')
out_file.write(str(final))

out_file.write('\n\n')
out_file.write('2) Analysis of Hill Climbing:-')

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


###     BELOW IS CODE TO GET OUTPUT ON TERMINAL     ###

# print('1) Analysis for Best First Search:-')
# BM_pathlen, BM_status, final = BeFS(start, goal, manhattan)
# print('\t(i)Manhattan:-')
# print('\t\tStates explored:-', BM_pathlen)
# if BM_status:
#     print('\t\tCompletion status:- Reached GOAL state')
# else:
#     print('\t\tCompletion status:- Cannot reach GOAL state')
# print ('\t\tFinal State = ', final)


# BO_pathlen, BO_status, final = BeFS(start, goal, oneadder)
# print('\t(ii)One Adder:-')
# print('\t\tStates explored:-', BO_pathlen)
# if BO_status:
#     print('\t\tCompletion status:- Reached GOAL state')
# else:
#     print('\t\tCompletion status:- Cannot reach GOAL state')
# print ('\t\tFinal State = ', final)


# BL_pathlen, BL_status, final = BeFS(start, goal, leveladder)
# print('\t(iii)Level Adder:-')
# print('\t\tStates explored:-', BL_pathlen)
# if BL_status:
#     print('\t\tCompletion status:- Reached GOAL state')
# else: 
#     print('\t\tCompletion status:- Cannot reach GOAL state')
# print ('\t\tFinal State = ', final)


# print('\n')
# print('2) Analysis for Hill Climbing:-')
# HM_pathlen, HM_status, final = hillClimbing(start, goal, manhattan)
# print('\t(i)Manhattan:-')
# print('\t\tStates explored:-', HM_pathlen)
# if HM_status:
#     print('\t\tCompletion status:- Reached GOAL state')
# else:
#     print('\t\tCompletion status:- Cannot reach GOAL state')
# print ('\t\tFinal State = ', final)


# HO_pathlen, HO_status, final = hillClimbing(start, goal, oneadder)
# print('\t(ii)One Adder:-')
# print('\t\tStates explored:-', HO_pathlen)
# if HO_status:
#     print('\t\tCompletion status:- Reached GOAL state')
# else:
#     print('\t\tCompletion status:- Cannot reach GOAL state')
# print ('\t\tFinal State = ', final)


# HL_pathlen, HL_status, final = hillClimbing(start, goal, leveladder)
# print('\t(iii)Level Adder:-')
# print('\t\tStates explored:-', HL_pathlen)
# if HL_status:
#     print('\t\tCompletion status:- Reached GOAL state')
# else:
#     print('\t\tCompletion status:- Cannot reach GOAL state')
# print ('\t\tFinal State = ', final)

"""
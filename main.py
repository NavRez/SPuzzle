import copy
import time
# make a DFS algorithm for the S Puzzle
# to do so, you will need to start out with the smallest index value and go to the greatest
# prioritize left, down, right and up in that order : make sure these are functions
# make it recursive

goal = (
    (1, 2, 3), 
    (4, 5, 6), 
    (7, 8, 9)
    )
goal16 = (
    (1, 2, 3, 4), 
    (5, 6, 7, 8), 
    (9, 10, 11, 12),
    (13, 14, 15, 16)
    )
goal25 = (
    (1, 2, 3, 4, 5), 
    (6, 7, 8, 9, 10), 
    (11, 12, 13, 14, 15),
    (16, 17, 18, 19, 20),
    (21, 22, 23, 24, 25)
    )
start = [
    [5, 3, 9], 
    [4, 2, 8], 
    [6, 1, 7]
    ]



class DFS:

    def __init__(self, start, goal):
        self.start = start
        self.goal = goal
        self.path = []
        self.order = []
        self.closed = []
        self.opened = []
        self.numericalDict = dict()
        count = 1
        rowc = 0
        for row in goal:
            colc = 0
            for placement in row:
                self.order.append(placement)
                self.numericalDict[count] = [rowc,colc]
                colc+=1
                count+=1
            rowc+=1

    def solve(self,currentNum,currentState,start,originalstate,isFound):

        if len(self.closed) == 0:
            currentState = self.opened.pop(0) # the target state that you wish to reach
            self.path.append(currentState)
            self.closed = originalstate
            self.closed.append(currentState)
            movelist = self.categorize(currentState[0],currentState[1])
            if self.numericalDict[currentNum] == currentState:
                isFound[0] = True
        else:
            movelist = self.categorize(currentState[0],currentState[1])
    
        while len(movelist) != 0:
            forcount = 0
            for move in movelist:
                if not isFound[0]:
                    newstart = copy.deepcopy(start)
                    if move in self.closed:
                        forcount+=1
                    else:
                        self.swap(currentState,move,newstart)
                        self.path.append(move)

                        if self.numericalDict[currentNum] == move:
                            isFound[0] = True
                            self.start = newstart
                            break
                        else:
                            while forcount > 0:
                                movelist.pop(0)
                                forcount-=1
                            closed_node = movelist.pop(0)
                            if closed_node not in self.closed:
                                self.closed.append(closed_node)
                            self.solve(currentNum,closed_node,newstart,originalstate,isFound)
                            if not isFound[0]:
                                self.path.append(currentState)
                    if forcount == len(movelist):
                        movelist = list()
                else:
                    movelist = list()                    
            

    def swap(self,orgstate, newstate,start):
        val1 = start[orgstate[0]][orgstate[1]]
        val2 = start[newstate[0]][newstate[1]]
        start[orgstate[0]][orgstate[1]] = val2
        start[newstate[0]][newstate[1]] = val1
        

    def iterate(self):
        permlist = list()
        allpaths = [[],[]]
        counting = 1
        starttime = time.time()
        f = open("dfspath.txt", "a")
        f2 = open("dfssol.txt", "a")
        f.write("***************************************************************\n")
        f.write("%s\n" %(str(self.start)))
        f2.write("***************************************************************\n")
        f2.write("%s\n" %(str(self.start)))
        print("starting DFS...")
        while len(self.order)> 0:

            target = self.order.pop(0)

            rowind = 0
            colind = 0

            found =False
            for row in self.start:
                for loc in row:
                    if loc == target:
                        rowind = self.start.index(row)
                        colind = row.index(loc)
                        found = True
                        break
                if found:
                    break
            found = [False]
            self.opened.append([rowind,colind])
            self.solve(target,[rowind,colind],self.start,permlist,found)
            self.opened = list()
            self.closed = list()
            sol = list()
            for direction in self.path:
                if direction not in sol:
                    sol.append(direction)
            solu = list()
            for i in range(len(sol)-1,-1,-1): #direction in self.path:
                if len(solu) != 0 and sol[i] not in solu:
                    d = abs(solu[0][0] - sol[i][0]) +abs(solu[0][1] - sol[i][1])
                    if d == 1:
                        solu.insert(0,sol[i])
                elif len(solu) == 0:
                    solu.append(sol[i])
            allpaths[0].append(self.path)
            allpaths[1].append(solu)
            self.path = list()
            permlist = list()
            counting+=1
            for i in range(1,counting):
                permlist.append(self.numericalDict[i])
        endtime = time.time()
        print("ended with time : " + str((endtime -starttime)))

        count = 1
        for paths in allpaths[0]:
            f.write("%d : %s\n" %(count,str(paths)))
            count+=1
        count = 1
        for sols in allpaths[1]:
            f2.write("%d : %s\n" %(count,str(sols)))
            count+=1
        f.write("***************************************************************\n")
        f2.write("***************************************************************\n")



    def categorize(self,rowind,colind):
        templist = list()
        if rowind == 0:

            if colind == 0:
                down = [rowind+1,colind]
                right = [rowind,colind+1]
                templist.extend([down,right])
            elif colind == len(start)-1:
                left = [rowind,colind-1]
                down = [rowind+1,colind]
                templist.extend([left,down])
            else:
                left = [rowind,colind-1]
                down = [rowind+1,colind]
                right = [rowind,colind+1]
                templist.extend([left,down,right])

        elif rowind == len(start)-1:

            if colind == 0:
                right = [rowind,colind+1]
                up = [rowind-1,colind]
                templist.extend([right,up])
            elif colind == len(start)-1:
                left = [rowind,colind-1]
                up = [rowind-1,colind]
                templist.extend([left,up])
            else:
                left = [rowind,colind-1]
                right = [rowind,colind+1]
                up = [rowind-1,colind]
                templist.extend([left,right,up])

        else:
            
            if colind == 0:
               down = [rowind+1,colind]
               right = [rowind,colind+1]
               up = [rowind-1,colind]
               templist.extend([down,right,up])
            elif colind == len(start)-1:
               left = [rowind,colind-1] 
               down = [rowind+1,colind]
               up = [rowind-1,colind]
               templist.extend([left,down,up])
            else:
               left = [rowind,colind-1] 
               down = [rowind+1,colind]
               right = [rowind,colind+1]
               up = [rowind-1,colind]
               templist.extend([left,down,right,up])
        
        return templist

class IterativeDeepening:

    def __init__(self, start, goal):
        self.start = start
        self.depth = 0
        self.goal = goal
        self.path = []
        self.solpath  = []
        self.order = []
        self.closed = []
        self.opened = []
        self.numericalDict = dict()
        count = 1
        rowc = 0
        for row in goal:
            colc = 0
            for placement in row:
                self.order.append(placement)
                self.numericalDict[count] = [rowc,colc]
                colc+=1
                count+=1
            rowc+=1

    def swap(self,orgstate, newstate,start):
        val1 = start[orgstate[0]][orgstate[1]]
        val2 = start[newstate[0]][newstate[1]]
        start[orgstate[0]][orgstate[1]] = val2
        start[newstate[0]][newstate[1]] = val1

    def solve(self,currentNum,currentState,start,originalstate,isFound,depthLimit):
        if depthLimit >= 0:
            depthLimit-=1
            if len(self.closed) == 0:
                currentState = self.opened.pop(0) # the target state that you wish to reach
                self.path.append(currentState)
                self.closed = originalstate
                self.closed.append(currentState)
                movelist = self.categorize(currentState[0],currentState[1])
                if self.numericalDict[currentNum] == currentState:
                    isFound[0] = True
            else:
                movelist = self.categorize(currentState[0],currentState[1])
        
            while len(movelist) != 0:
                forcount = 0
                for move in movelist:
                    if not isFound[0]:
                        newstart = copy.deepcopy(start)
                        if move in self.closed:
                            forcount+=1
                        else:
                            self.swap(currentState,move,newstart)
                            self.path.append(move)

                            if self.numericalDict[currentNum] == move:
                                isFound[0] = True
                                self.start = newstart
                                self.solpath.append(currentState)
                                break
                            else:
                                while forcount > 0:
                                    movelist.pop(0)
                                    forcount-=1
                                closed_node = movelist.pop(0)
                                if closed_node not in self.closed:
                                    self.closed.append(closed_node)
                                self.solve(currentNum,closed_node,newstart,originalstate,isFound,depthLimit)
                                if not isFound[0]:
                                    self.path.append(currentState)
                        if forcount == len(movelist):
                            movelist = list()
                    else:
                        movelist = list()
                        self.solpath.append(currentState)     


    def iterate(self):
        permlist = list()
        allpaths = [[],[]]
        counting = 1
        starttime = time.time()
        f = open("idpath.txt", "a")
        f2 = open("idssol.txt", "a")
        f.write("***************************************************************\n")
        f.write("%s\n" %(str(self.start)))
        f2.write("***************************************************************\n")
        f2.write("%s\n" %(str(self.start)))
        older = copy.deepcopy(self.order)
        print("starting IDDFS...")
        depth = self.depth
        while len(self.order)> 0:

            target = self.order.pop(0)

            rowind = 0
            colind = 0

            found =False
            for row in self.start:
                for loc in row:
                    if loc == target:
                        rowind = self.start.index(row)
                        colind = row.index(loc)
                        found = True
                        break
                if found:
                    break
            found = [False]
            self.opened.append([rowind,colind])
            self.solve(target,[rowind,colind],self.start,permlist,found,depth)
            self.opened = list()
            self.closed = list()
            permlist = list()
            if found[0] == True:
                counting+=1
                for i in range(1,counting):
                    permlist.append(self.numericalDict[i])
                depth = 0
                older = copy.deepcopy(self.order)
                sol = list()
                for direction in self.path:
                    if direction not in sol:
                        sol.append(direction)
                solu = list()
                for i in range(len(sol)-1,-1,-1): #direction in self.path:
                    if len(solu) != 0 and sol[i] not in solu:
                        d = abs(solu[0][0] - sol[i][0]) +abs(solu[0][1] - sol[i][1])
                        if d == 1:
                            solu.insert(0,sol[i])
                    elif len(solu) == 0:
                        solu.append(sol[i])
                allpaths[0].append(self.path)
                allpaths[1].append(solu)
            else:
                self.order = copy.deepcopy(older)
                depth+=1
            self.path = list()
        endtime = time.time()
        print("ended with time : " + str((endtime -starttime)))

        count = 1
        for paths in allpaths[0]:
            f.write("%d : %s\n" %(count,str(paths)))
            count+=1
        count = 1
        for sols in allpaths[1]:
            f2.write("%d : %s\n" %(count,str(sols)))
            count+=1
        f.write("***************************************************************\n")
        f2.write("***************************************************************\n")


               


    def categorize(self,rowind,colind):
        templist = list()
        if rowind == 0:

            if colind == 0:
                down = [rowind+1,colind]
                right = [rowind,colind+1]
                templist.extend([down,right])
            elif colind == len(start)-1:
                left = [rowind,colind-1]
                down = [rowind+1,colind]
                templist.extend([left,down])
            else:
                left = [rowind,colind-1]
                down = [rowind+1,colind]
                right = [rowind,colind+1]
                templist.extend([left,down,right])

        elif rowind == len(start)-1:

            if colind == 0:
                right = [rowind,colind+1]
                up = [rowind-1,colind]
                templist.extend([right,up])
            elif colind == len(start)-1:
                left = [rowind,colind-1]
                up = [rowind-1,colind]
                templist.extend([left,up])
            else:
                left = [rowind,colind-1]
                right = [rowind,colind+1]
                up = [rowind-1,colind]
                templist.extend([left,right,up])

        else:
            
            if colind == 0:
               down = [rowind+1,colind]
               right = [rowind,colind+1]
               up = [rowind-1,colind]
               templist.extend([down,right,up])
            elif colind == len(start)-1:
               left = [rowind,colind-1] 
               down = [rowind+1,colind]
               up = [rowind-1,colind]
               templist.extend([left,down,up])
            else:
               left = [rowind,colind-1] 
               down = [rowind+1,colind]
               right = [rowind,colind+1]
               up = [rowind-1,colind]
               templist.extend([left,down,right,up])
        
        return templist

class Aster:

    def __init__(self, start, goal):
        self.start = start
        self.depth = 0
        self.goal = goal
        self.path = []
        self.order = []
        self.closed = []
        self.opened = []
        self.numericalDict = dict()
        count = 1
        rowc = 0
        for row in goal:
            colc = 0
            for placement in row:
                self.order.append(placement)
                self.numericalDict[count] = [rowc,colc]
                colc+=1
                count+=1
            rowc+=1

    def swap(self,orgstate, newstate,start):
        val1 = start[orgstate[0]][orgstate[1]]
        val2 = start[newstate[0]][newstate[1]]
        start[orgstate[0]][orgstate[1]] = val2
        start[newstate[0]][newstate[1]] = val1

    def manhattan(self,curpos,goalpos):
        distance = abs(curpos[0] - goalpos[0]) + abs(curpos[1] - goalpos[1])
        return distance

    def disorder(self,start,curpos,goalpos,currnum):
        dist = 0
        for i in range(curpos[0],-1,-1):
            for j in range(len(start)-1,-1,-1):
                if start[i][j] > currnum:
                    if i == curpos[0]: 
                        if j < curpos[1]:
                            dist+=1
                    else:
                        dist+=1
        return dist


    def heuristic1(self,currentNum,currentState,start,originalstate,isFound,mandist):
        newmandist = self.manhattan(currentState,self.numericalDict[currentNum])
        if mandist >= newmandist:
            if len(self.closed) == 0:
                currentState = self.opened.pop(0) # the target state that you wish to reach
                self.path.append(currentState)
                self.closed = originalstate
                self.closed.append(currentState)
                movelist = self.categorize(currentState[0],currentState[1])
                if self.numericalDict[currentNum] == currentState:
                    isFound[0] = True
            else:
                movelist = self.categorize(currentState[0],currentState[1])
        
            while len(movelist) != 0:
                forcount = 0
                for move in movelist:
                    if not isFound[0]:
                        newstart = copy.deepcopy(start)
                        if move in self.closed:
                            forcount+=1
                        else:
                            self.swap(currentState,move,newstart)
                            self.path.append(move)

                            if self.numericalDict[currentNum] == move:
                                isFound[0] = True
                                self.start = newstart
                                break
                            else:
                                while forcount > 0:
                                    movelist.pop(0)
                                    forcount-=1
                                closed_node = movelist.pop(0)
                                if closed_node not in self.closed:
                                    self.closed.append(closed_node)
                                self.heuristic1(currentNum,closed_node,newstart,originalstate,isFound,newmandist)
                                if not isFound[0]:
                                    self.path.append(currentState)
                        if forcount == len(movelist):
                            movelist = list()
                    else:
                        movelist = list()     
        else:
            if currentState not in self.closed:
                self.closed.append(currentState)
    
    def finalsolve(self,currentNum,currentState,start,originalstate,isFound,mandist):
        newmandist = self.disorder(start,currentState,self.numericalDict[currentNum],currentNum)
        if mandist >= newmandist:
            if len(self.closed) == 0:
                currentState = self.opened.pop(0) # the target state that you wish to reach
                self.path.append(currentState)
                self.closed = originalstate
                self.closed.append(currentState)
                movelist = self.categorize(currentState[0],currentState[1])
                if self.numericalDict[currentNum] == currentState:
                    isFound[0] = True
            else:
                movelist = self.categorize(currentState[0],currentState[1])
        
            while len(movelist) != 0:
                forcount = 0
                for move in movelist:
                    if not isFound[0]:
                        newstart = copy.deepcopy(start)
                        if move in self.closed:
                            forcount+=1
                        else:
                            self.swap(currentState,move,newstart)
                            self.path.append(move)

                            if self.numericalDict[currentNum] == move:
                                isFound[0] = True
                                self.start = newstart
                                break
                            else:
                                while forcount > 0:
                                    movelist.pop(0)
                                    forcount-=1
                                closed_node = movelist.pop(0)
                                if closed_node not in self.closed:
                                    self.closed.append(closed_node)
                                self.finalsolve(currentNum,closed_node,newstart,originalstate,isFound,mandist)
                                if not isFound[0]:
                                    self.path.append(currentState)
                        if forcount == len(movelist):
                            movelist = list()
                    else:
                        movelist = list()     
        else:
            if currentState not in self.closed:
                self.closed.append(currentState)



    def phoenix(self): # heuristic 1 : the manhattan distance
        permlist = list()
        allpaths = [[],[]]
        counting = 1
        starttime = time.time()
        f = open("h1path.txt", "a")
        f2 = open("h1sol.txt", "a")
        f.write("***************************************************************\n")
        f.write("%s\n" %(str(self.start)))
        f2.write("***************************************************************\n")
        f2.write("%s\n" %(str(self.start)))
        print("starting h1...")
        while len(self.order)> 0:

            target = self.order.pop(0)

            rowind = 0
            colind = 0

            found =False
            for row in self.start:
                for loc in row:
                    if loc == target:
                        rowind = self.start.index(row)
                        colind = row.index(loc)
                        found = True
                        break
                if found:
                    break
            found = [False]
            self.opened.append([rowind,colind])
            currDist = self.manhattan([rowind,colind],self.numericalDict[counting])
            self.heuristic1(target,[rowind,colind],self.start,permlist,found,currDist)
            self.opened = list()
            self.closed = list()
            sol = list()
            for direction in self.path:
                if direction not in sol:
                    sol.append(direction)
            solu = list()
            for i in range(len(sol)-1,-1,-1): #direction in self.path:
                if len(solu) != 0 and sol[i] not in solu:
                    d = abs(solu[0][0] - sol[i][0]) +abs(solu[0][1] - sol[i][1])
                    if d == 1:
                        solu.insert(0,sol[i])
                elif len(solu) == 0:
                    solu.append(sol[i])
            allpaths[0].append(self.path)
            allpaths[1].append(solu)
            self.path = list()
            permlist = list()
            counting+=1
            for i in range(1,counting):
                permlist.append(self.numericalDict[i])
        endtime = time.time()
        print("ended with time : " + str((endtime -starttime)))

        count = 1
        for paths in allpaths[0]:
            f.write("%d : %s\n" %(count,str(paths)))
            count+=1
        count = 1
        for sols in allpaths[1]:
            f2.write("%d : %s\n" %(count,str(sols)))
            count+=1
        f.write("***************************************************************\n")
        f2.write("***************************************************************\n")

    def heuristic2 (self):
        permlist = list()
        allpaths = [[],[]]
        counting = 1
        starttime = time.time()
        f = open("h2path.txt", "a")
        f2 = open("h2sol.txt", "a")
        f.write("***************************************************************\n")
        f.write("%s\n" %(str(self.start)))
        f2.write("***************************************************************\n")
        f2.write("%s\n" %(str(self.start)))
        print("starting h2...")
        while len(self.order)> 0:

            target = self.order.pop(0)

            rowind = 0
            colind = 0

            found =False
            for row in self.start:
                for loc in row:
                    if loc == target:
                        rowind = self.start.index(row)
                        colind = row.index(loc)
                        found = True
                        break
                if found:
                    break
            found = [False]
            self.opened.append([rowind,colind])
            currDist = self.disorder(self.start,[rowind,colind],self.numericalDict[counting],target)
            self.finalsolve(target,[rowind,colind],self.start,permlist,found,currDist)
            self.opened = list()
            self.closed = list()
            sol = list()
            for direction in self.path:
                if direction not in sol:
                    sol.append(direction)
            solu = list()
            for i in range(len(sol)-1,-1,-1): #direction in self.path:
                if len(solu) != 0 and sol[i] not in solu:
                    d = abs(solu[0][0] - sol[i][0]) +abs(solu[0][1] - sol[i][1])
                    if d == 1:
                        solu.insert(0,sol[i])
                elif len(solu) == 0:
                    solu.append(sol[i])
            allpaths[0].append(self.path)
            allpaths[1].append(solu)
            self.path = list()
            permlist = list()
            counting+=1
            for i in range(1,counting):
                permlist.append(self.numericalDict[i])
        endtime = time.time()
        print("ended with time : " + str((endtime -starttime)))

        count = 1
        for paths in allpaths[0]:
            f.write("%d : %s\n" %(count,str(paths)))
            count+=1
        count = 1
        for sols in allpaths[1]:
            f2.write("%d : %s\n" %(count,str(sols)))
            count+=1
        f.write("***************************************************************\n")
        f2.write("***************************************************************\n")

    def categorize(self,rowind,colind):
        templist = list()
        if rowind == 0:

            if colind == 0:
                down = [rowind+1,colind]
                right = [rowind,colind+1]
                templist.extend([down,right])
            elif colind == len(start)-1:
                left = [rowind,colind-1]
                down = [rowind+1,colind]
                templist.extend([left,down])
            else:
                left = [rowind,colind-1]
                down = [rowind+1,colind]
                right = [rowind,colind+1]
                templist.extend([left,down,right])

        elif rowind == len(start)-1:

            if colind == 0:
                up = [rowind-1,colind]
                right = [rowind,colind+1]
                templist.extend([right,up])
            elif colind == len(start)-1:
                up = [rowind-1,colind]
                left = [rowind,colind-1]
                templist.extend([left,up])
            else:
                up = [rowind-1,colind]
                left = [rowind,colind-1]
                right = [rowind,colind+1]
                templist.extend([left,right,up])

        else:
            
            if colind == 0:
               up = [rowind-1,colind]
               down = [rowind+1,colind]
               right = [rowind,colind+1]
               templist.extend([down,right,up])
            elif colind == len(start)-1:
               up = [rowind-1,colind]
               left = [rowind,colind-1] 
               down = [rowind+1,colind]
               templist.extend([left,down,up])
            else:
               up = [rowind-1,colind]
               left = [rowind,colind-1] 
               down = [rowind+1,colind]
               right = [rowind,colind+1]
               templist.extend([left,down,right,up])
        
        return templist

            

    



n = int(input("Enter the n value : "))
#file = open('24rand.txt', 'r')
#file = open('15rand.txt', 'r')
file = open('random.txt', 'r')
Lines = file.readlines()
starts = list()

for line in Lines:
    line.strip()
    x = line.split()
    subgoal = list()
    newgoal = list()
    count = 1
    for number in x:
        subgoal.append(int(number))
        count+=1
        if count > n:
            newgoal.append(subgoal)
            count = 1
            subgoal = list()
    starts.append(newgoal)

f = open("idpath.txt", "w")
f.write("")
f2 = open("idssol.txt", "w")
f2.write("")
f = open("dfspath.txt", "w")
f.write("")
f2 = open("dfssol.txt", "w")
f2.write("")
f = open("h1path.txt", "w")
f.write("")
f2 = open("h1sol.txt", "w")
f2.write("")
f = open("h2path.txt", "w")
f.write("")
f2 = open("h2sol.txt", "w")
f2.write("")

count = 0
#goal = goal16
#goal = goal25
for start in starts:
    print("iteration " + str(count))
    idf = IterativeDeepening(start,goal)
    idf.iterate()

    dfs = DFS(start,goal)
    dfs.iterate()
    count+=1

    aster  = Aster(start,goal)
    aster.phoenix()

    blaster  = Aster(start,goal)
    blaster.heuristic2()
    print("\n")

#RecurseTest(integer=10)


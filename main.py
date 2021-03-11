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
start = [
    [9, 8, 7], 
    [6, 4, 5], 
    [1, 2, 3]
    ]



class DFS:

    def __init__(self, start, goal):
        self.start = start
        self.goal = goal
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
        counting = 1
        starttime = time.time()
        print("starting ...")
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
            permlist = list()
            counting+=1
            for i in range(1,counting):
                permlist.append(self.numericalDict[i])
        endtime = time.time()
        print("ended with time : " + str((endtime -starttime)))



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
        self.goal = goal
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
            

    


# def RecurseTest(integer):
#     if integer > 1:
#         RecurseTest(integer-1)
#     print(integer)

df = DFS(start,goal)
df.iterate()

#RecurseTest(integer=10)


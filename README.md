# SPuzzle

## Purpose
The primary objective of this project was to test out a modified version of the sliding tile puzzle also known as the 8-Puzzle into an S-puzzle, where every single block in an NxN matrix can be moved to an adjacent block. The goal being to sort an NxN matrix to an increasing order with 6 different algorithms : heursitic Depth-FIrst Search, heuristic Iterative Deepening, and two heuristic algorithms of our choice. There is also a true DFS and a true IDDFS (non-heuristic)

## Heuristics
The first heuristic was the block distance, which would evaluate the distance between a block and its intended position in terms of rows and columns, with the sum of both distances being the block distance. The algorithm will then try to iterate through several moves as long as it decreases the block distance from its prior value (this is done in a recursive fashion).
The second heuristic calculates the number of misplaced tiles from a block's position (ex: say you're given 54321 and need to sort 1, then there are 4 misplaced values because 1 is smaller than all of them), this algorithm will go a certain direction as long as the new distance is smaller than the original one.
It should be noted that there are two other heuristics in this problem. They are mistakenly known as the "dfs" and "iddfs" , when in reality it's actually a heuristic dfs and a heuristic iddfs. They operate by informing the class about the real position of a number (in increasing order), the algorithm then applies a heuristic dfs or heuristic iddfs on each individual number until it's sorted (ex: for 543216789, the number 1 currently at position [1,1] will go through various movements until it's in position [0,0] and then break to allow  the next number to be sorted)

## How to execute
Make sure you place every single file in the same folder. Ensure that the python that you're using is 3.8 and above, install any missing libraries indicated in the import section above the main file. The default file that will be read is the random.txt file. Once the program runs it will ask the user for the value of n (which is 3 for the random.txt, 4 for 15rand.txt and 5 for 24rand.txt). These values are not autogenerated and need to be entered manually when the question appears in the terminal.
Once the value has been entered (3 under the default settings), this will execute the program and calculate the execution values for 20 different randomly generate values ranging from 1 to 9. It should be noted that non of the non-heurisitc functions will be able to solve any puzzle due to the 60 second time contraint, therefore it may take well over 40 minutes for the algorithm to show any results. To bypass this, comment out lines 1024 to 1036, these are the non-heuristic functions

## Scaling up
1.If you wish to scale up the algorithm , comment out the "file = open('random.txt', 'r')", then uncomment "file = open('15rand.txt', 'r')" and "goal = goal16". this will allow you to scale up to S = 4. 
2.Comment out the "file = open('random.txt', 'r')", then uncomment "file = open('24rand.txt', 'r')" and "goal = goal24". this will allow you to scale up to S = 5.

You cannot uncomment both of these at the same time, if you wish to view S = 5, only comment out the values indicated in 2) and comment all those in 1). If you wish to view S = 4, only comment out the values indicated in 1) and comment all those in 2) 

Comment out lines 1024 to 1036, it is unlikely that these non-heuristic functions will be able to find a solution

## Output files

Two output files will be generated by all four algorithms , a solution path and a search path. All solution paths end with sol while all search paths end with path. 

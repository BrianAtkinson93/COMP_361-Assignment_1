# Assignment 1 (Grassfire Algorithm)

---
Brian Atkinson <br>
300088157 <br>
Tuesday Jan 17, 2023 <br>
COMP_361 <br>
Amir Shabani, PhD. P.Eng

---
## Build
In order to build the package it is recommended to start a python venv. Then run the following commands.
```bash
# Install all the required packages to build the binary
pip install -r Requirements.txt
```
```bash
# Command to build the gui. Places the file in <cwd>/dist/simulation
pyinstaller simulation.spec
```
```bash
# you can also build and run the commandline version
pyinstaller grassfire_simulation.spec
# Run the usage and help command
./dist/grassfire_simulation -h 
```

## Run
This program is easy to run, the -h flag can be set for quick reminders.
example of execution after build:
```bash
./dist/simulation

# You can also run the original cmd-line based program
./dist/grassfire_simulation 15 20 -o 10
# The first two positional arguments are columns and rows respectively.
# the --obstacles flag can be set to change the % of obstacles populated 
# from default value of 10
```

## Contributors
Project Lead: Amir Shabani <br>
Lead Developer: Brian Atkinson<br>

---

## ASSIGNMENT GUIDLINES
## Objective: 
Examine a graph-based path planning algorithm for robot motion planning. 

Note: This lab will be marked out 100 and has 20 mark as bonus (part 3). Please read the instruction at the end of this file for submission of your files/codes and also the video recording. 

## Part1 [20 marks]: 
A robot is constrained to move in the given 2D grid and not hitting the obstacles/barriers (i.e., black cells). Use the Grassfire algorithm and find all the shortest paths that the robot could take to go from the START node (Green) to the GOAL node (Red). 
You need to do this part by hand and identify all the possible path solutions.

## Part2 [80 marks]: 
Write a program (preferably in Python, if not Java) which automatically generates the search map for the robot and then finds the shortest path using Grassfire algorithm. 

Here are the steps to generate the search map based on the inputs from the user:
a.	Step1: divide the search region in grid cells: 
User enters the size of the region as the dimensions of the grid. This means user should provide the number of rows and columns. The minimum size should be 8x8.
b.	Step 2: identify the obstacle cells
Use provides a random number as the percentage of the obstacle cells. This can be any percentage in the range of 10% to 20%. In your program, you can round up the user input to make it an integer number. Based on this number, generate a random list of pairs representing the row and column indices of the obstacle cells.
c.	Step 3: initialize the starting cell
User enters a random number less than the number of columns which represents a cell in the first row as the starting cell/node.
d.	Step 4: initialize the destination cell
User provides the index of row and column for the destination node. To this end, the row index should be a random number greater than half of the number of rows (i.e., if the number of rows is 10, the row index for the destination cell should be greater than 5) and the column index is greater than 2/3 of the number of columns (i.e., if the number of columns is 10, the column index for the destination cell should be greater than 6.6 which should be round up to 7).


The program should output the searched map (graphically or in matrix format) and then print the solutions corresponding to the shortest path(s) using Grassfire algorithm.

## Part 3[Bonus 20 marks]: 
Make a GUI for part 2 with a nice graphics for the search map and also the results. 



## Submissions:

1.	Please submit your work (files and codes) on BB under “Course Content/Student Submissions” folder. 
2.	You also need to record a video (roughly about 3min, not more than 5min) and demo your code for part 2. 
You need to explains clearly your approach, run your code, and demonstrate your solution. Provide the link to your video (on Youtube/Vimeo/GoogleDrive…) in the body of your submission. Make sure the like in accessible for me to watch to evaluate your work.

The video component is worth 60% of the mark for part 2 of the assignment.



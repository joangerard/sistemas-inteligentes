# Help Mario to Get Out!

Mario is trapped in a weird world so let's help him to get out from there. 

## Problem-solver agent design

&emsp;The agent is designed as follows.

### Objective Formulation

&emsp;Mario arrives to the shortest pipe whenever is possible.

### Problem Formulation
&emsp;**Initial State:** Current map configuration + Mario's position

&emsp;**Goal State:** Current map configuration + Mario's positioned into the shortest pipe

&emsp;**Goal Test** Is Mario positioned into the shortest pipe?

&emsp;**Actions:** Move Mario up, down, left, right whenever possible.

&emsp;**Transition Function:** Giving Mario's position move him up, down, left, right to get a new Mario's position.

&emsp;**Cost:** 1

### Search, Solve and Execute

&emsp;Using this problem-solver agent we can choose
BFS to search a path from Mario to the shortest pipe. 

_Why BFS?_

&emsp;Because it ensures to find an optimal solution and it is complete.
If we use DFS with the above problem-solver agent we would not end up finding the shortest path because
it is not optimal.


---

## Practical solution to the problem

We need to clarify that the solution presented below does not align with the problem-solver agent defined above.
This is because the problem definition adds an extra requirement and this is to pre-calculate
the number of squares that Mario needs to cross for every empty square. If we had not had this 
extra requirement we would have been able to implement that problem-solver agent.

The map is represented by a 2d array: 

```
[[inf,  -1, inf,   0],
 [inf, inf, inf,  -1],
 [inf,  -1, inf,  -1],
 [0  ,  -1, inf, inf]]
```

Where the empty spaces are represented by a big number `inf`, the walls by `-1` and the pipes by `0` (notice that 
Mario's position is not represented in the map).

The first thing we are going to do is to use a search algorithm to build a new map. For each empty square `x` 
we are going to through a number `n` that indicates how far Mario is from `x` to the shortest pipe.

We can use BFS, DFS, or ID to build such map, each one of them has it's own pros and cons.
 
 - DFS uses linear memory but this algorithm applied to this kind of problem recomputes the path 
 for each pipe and see if that path is better to the current one which is not very practical. 
 - BFS uses exponential memory but this algorithm can compute the numbers in one pass.
 - ID has no real benefits over BFS and DFS for this case since we still need to traverse all the states anyway. 
 
 So I chose to use BFS due to the simplicity of the implementation and the resemblance to 
 the code that we have seen in class.
 
 The idea behind it is to put the pipe's position into the queue and run BFS incrementing a counter 
 from the previously visited state. The count starts from the pipes' position and not from Mario's. That's the trick to
 run BFS smoothly on this one. 
 
Once we have built the new map and given Mario's position we can just run a not-provided-with-intelligence 
algorithm to go from Mario's position to the shortest path selecting the neighbor square with minimum `n`.

And voilá! We have solved the assignment. 

___

## Porotos
In the worst-case scenario the problem-solver agent
will expand all the states in the state space. 
Since we are using BFS, this is _O_(b^d). :trollface:

---
## Installation Guide

You need to have installed in your local machine:
```
python 3.7
numpy library
```

To run the project execute: 
```
$python main.py
```


# AI

## After spending hundreds hours on playing, let's try to write a bot playing game and beating our highscores :)

### Interface

After every move, you get the info about:
+ possible direction of move
+ your move
+ your current result (in %)
+ potential score after each possible move

In **grid.py** method _data_ returns all needed data 

Then, you are to return one of 4 values - 0, 1, 2 or 3, meaning following directions: up, down, right left
If you try to do an invalid move, a play on this grid will end, and next grid will be tested.

### Test

Run 
```
python3 main.py
``` 
for testing all methods declared in **ai.py**

### Create
In **ai.py** there are some functions implementing simply tactics.
There you can add yours.
In **main.py** 
```python
methods = [random, first, greed]
```
_methods_ contains all names of method to test. Put there everything you want to test

### Summary

Example of result:
```
Name    Avg(%)  Min(%)  Max(%)  StDev   Fail AvgSteps
random  2.042   0.308   6.119   1.295   0    34.21
first   9.572   0.385   24.842  5.585   0    50.33
greed   2.827   0.366   10.647  1.722   0    31.11
```
Column **Fail** indicates how many times your bot tried to move incorrectly. 

#### Grids

File **grids.txt** contains 100 generated grids. See **generator** branch for more info

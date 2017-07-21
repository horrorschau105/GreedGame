# GreedGame
Idea taken from: http://www.catb.org/esr/greed/

### Run:
```
python3 main.py
```
### Moving

Control - arrows
Your position - indicated by *@*, and at the bottom by two numbers. At game over - *@* turns into *+*

### Rules

Numbers around your position say how far you have to move in corresponding direction.
You can't go through one cell more than once. Possible moves are shown at the bottom.

### Highscores
Highscores are stored in _highscores.xd_ in very simple way.

### Other branches

**generator** - contains generator for random grids.
**ai** - some implementations of simple bots playing GreedGame. Actually best reached results are in average 29%

# Grids Generator

### Usage:
```
python3 main.py (count of grids) (width) (height) (max value in single cell) > (output file)
```
i.e.
```
python3 main.py 100 100 100 9 > grids.txt
```

### Output:
Output file is represented as follows:

First number indicates count of grids.
Each grid is described this way:
(height) (width) (position.x) (position.y)
(_height_ lines of length _width_ containing numbers 1..._(max value in single cell)_

### Small example:

```
2
3 3 1 1 
122
222
211
4 4 2 2
1422
3222
1122
2322
```

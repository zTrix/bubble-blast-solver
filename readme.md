# Bubble Blast Solver

## Requirement
Python 2.7

## Usage
    python solve.py <input file> <touch count>

## Example
    python solve.py ./levels/1-32.in 3

## Note
- input file format as in.txt, 1 for red, 2 for green, 3 for yellow, 4 for blue
- output is zero indexed pair sequence, (row, colume), indicating the action sequence
- the bubble elimination logic of the game is really complex when dealing with a red bubble hit by more than one explosions, and this is why most bubble blast solver cannot solve all of the levels. I get the logic work by reverse engineering the Android apk file.

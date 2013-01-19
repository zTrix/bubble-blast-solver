# Bubble Blast Solver

## Requirement
Python

## Usage
    python solve.py <input file> <touch count>

## Example
    python solve.py ./levels/1-32.in 3

## Note
- input file format just as ./levels/*.txt, 1 for red, 2 for green, 3 for yellow, 4 for blue
- output is zero indexed pair sequence, (row, colume), indicating the action sequence
- the bubble elimination logic of the game is really complex when dealing with situations that a red bubble hit by more than one explosions, and this is why most bubble blast solver cannot solve all of the levels. I get the logic work by reverse engineering the Android apk file ([debugging patch](https://github.com/zTrix/bubble-blast-solver/blob/master/crack/bubbleblast-android-v1.0.31_mumayi_a9552.patch) ) and apply a simulation of its logic.
- The win8 version bubble blast has a different logic when dealing the situation, and the levels are differenct from Android and iOS. So my solver cannot solve all of win8 version levels.

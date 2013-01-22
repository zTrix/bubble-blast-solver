# Bubble Blast Solver

## Requirement
Python

## Usage
    $ python solve.py <input file> <touch count> [options]

options could be: -a -b
  -a switch on a special elimination logic for android
  -b switch on brute-force search path

## Example
    $ python solve.py ./levels/1-32.in 3

# About elimination logic
The bubble elimination logic of the game is really complex when dealing with situations that a red bubble hit by more than one explosions, and to make it worse, different game version(Android, iOS, Win 8) deals with it using different logic.

There is an example illustrating this logic problem: for level 1-50, the following click sequence can solve android version, but not iOS version:

    (0, 2)    (row, column), zero based, the third one in row one
    (4, 2)
    (4, 3)
    (3, 3)

This is why most bubble blast solver cannot solve all of the levels. I get the logic work by reverse engineering the Android apk file ([debugging patch](https://github.com/zTrix/bubble-blast-solver/blob/master/crack/bubbleblast-android-v1.0.31_mumayi_a9552.patch) ) and apply a simulation of its logic. 

So I wrote 2 elimination logic, one for normal version, and one for android specially. To enable the logic for Android, use -a switch like this:

    $ python solve.py ./levels/1-33.in 4 -a
    $ python solve.py ./levels/1-33.in 4 # (cannot find solution)
    $ python solve.py ./levels/1-33.in 5 # (can find solution)

## Note
- input file format just as ./levels/*.txt, 1 for red, 2 for green, 3 for yellow, 4 for blue
- output is zero indexed pair sequence, (row, colume), indicating the action sequence
- To speedup, pypy is highly recommended, with more than 5 times faster in average.


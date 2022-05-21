# Katamino
Katamino is a classic puzzle game. If unfamiliar the rules can be found [here](https://www.ultraboardgames.com/katamino/game-rules.php).  <br />
This Repository was created to get the solutions to any of the Katamino Challenges. <br >

## Intro to the Problem
There are 12 [free](https://en.wikipedia.org/wiki/Polyomino#Free,_one-sided,_and_fixed_polyominoes) pentaminoes and 
63 [fixed](https://en.wikipedia.org/wiki/Polyomino#Free,_one-sided,_and_fixed_polyominoes) pentaminoes. <br />
<br />
The goal of the game is given n number of free[pentaminoes](https://en.wikipedia.org/wiki/Pentomino) fit them in a nx5 rectangle. <br />
An eventual objective of this repository is to expnand this to get all solutions for any nxn space with <br />

## Starting out
1. Created the input file [Pentamino.txt](https://github.com/JoeyHinckley34/Katamino/blob/main/Pentamino.txt) which denoted the 12 fixed pentaminos as 1's and 0's. <br />
2. Read the input file and stored them as 2D arrays. For each matrix rotate four times transpose and rotate four more times to get every possible orientation and stored result into [allIters.txt](https://github.com/JoeyHinckley34/Katamino/blob/main/allIters.txt). This file contains 80 possible orientations, but there are only 63 free pentaminoes, so there are some duplicates!<br />
3. To get rid of duplicates the Pentamino class was born. Now that there is a class, the pentaminos can be hashed and quickly compared for equality. This allows this use of sets to get rid of any duplicate Pentamino's giving the set a size of the desired 63. A full explaination of how Pentaminos are hashed can be found [here](https://github.com/JoeyHinckley34/Katamino/blob/main/hashing.txt)
4. After getting all 63 Pentamino's hashed and in a set thier hashes were written to new text file, [hashedPentas.txt](https://github.com/JoeyHinckley34/Katamino/blob/main/hashedPentas.txt). This now serves as the input file. The reason we are going through all this trouble messing with our input file is for speed. Generating all possible iterations is computationally expense.
5. Now we can get to actually solving !

## The algorithm 
Right now we are brute forcing the living daylight out of it. <br />
Generating all possible positions of all input pentamino and storing each as a list. <br />
Cartesian multiply each list together to get every possible positioning for the given inputs. <br />
<br />
Drawbacks: Runtime <br />
Can be used to solve all 3x5 boards in reasonable <10 seconds, but any bigger and its not great. <br />
<br />
We are hoping to tranisiton into using [Knuth's Algorithm X](https://en.wikipedia.org/wiki/Knuth%27s_Algorithm_X)


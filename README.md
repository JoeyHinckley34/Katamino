# Katamino
Katamino is a classic puzzle game. If unfamiliar the rules can be found [here](https://www.ultraboardgames.com/katamino/game-rules.php).  <br />
This Repository was created to get the solutions to any of the Katamino Challenges. <br >

## Intro to the Problem
There are 12 [free](https://en.wikipedia.org/wiki/Polyomino#Free,_one-sided,_and_fixed_polyominoes) pentaminoes and 
63 [fixed](https://en.wikipedia.org/wiki/Polyomino#Free,_one-sided,_and_fixed_polyominoes) pentaminoes. <br />
<br />
The goal of the game is given n number of free[pentaminoes](https://en.wikipedia.org/wiki/Pentomino) fit them in a nx5 rectangle. <br />
An eventual objective of this repository is to expnand this to get all solutions for any nxn space with <br />

## Progress thus far
1. Created the input file [Pentamino.txt](https://github.com/JoeyHinckley34/Katamino/blob/main/Pentamino.txt) which denoted the 12 fixed pentaminos as 1's and 0's. <br />
2. Read the input file and stored them as 2D arrays. For each matrix rotate four times transpose and rotate four more times to get every possible orientation and stored result into [allIters.txt](https://github.com/JoeyHinckley34/Katamino/blob/main/allIters.txt). This file contains 80 possible orientations, but there are only 63 free pentaminoes, so there are some duplicates!<br />
3. To get rid of duplicates the Pentamino class was born. Now all that there is a class the pentaminos can be hashed and quickly compared for equality. A full explaination of how Pentaminos are hashed can be found [here](https://github.com/JoeyHinckley34/Katamino/blob/main/hashing.txt)

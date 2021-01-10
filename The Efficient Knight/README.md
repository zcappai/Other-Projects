# The Efficient Knight
This is an iterative program that calculates the minimum number of moves that a Knight can take between 2 chess tiles.

This program works by:
1. Starting at a specific tile and calculating all possible, legal moves from that tile.
2. For each of these moves, an array is created and stored in the main array. Each of these arrays stores a series of possible moves that the Knight can make during a game when moving between the source and destination tiles.
3. For the new tile in each of the arrays, the process is repeated.
4. Once an array has the destination tile as its newest tile, the program finishes as that array can be used to find the minimum number of moves.

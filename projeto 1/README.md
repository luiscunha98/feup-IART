# IART Assignment 1 - BOUND

## Work Done By: 

| GROUP  | 17 |
| ------------- | ------------- |
| Henrique Correia Vicente  | up202005321@up.pt  |
| Inês de Magalhães Garcia | up202004810@up.pt  |
| Luis Filipe Pinto Cunha | up201709375@up.pt

_________________________________________________________________________________________

## Description:

For the first IART project, the game we chose was BOUND, a Two-Player Adversarial Game.

Bound is a two player strategy game played on a single sheet of paper. Each turn, move one of your four standing stones in an attempt to encircle an opponent's stone.

Simple rules ensure that it is quick and easy to learn, but the unusual geometry of its pentacle-shaped board and the speed of its reversal of fortunes make Bound a dynamic and strategic contest.
_________________________________________________________________________________________


## How it works:
Our game is a 2D platformer where each player takes turns, moving one of your four standing stones in an attempt to encircle an opponent's stone.

Each player can only move their pieces to adjacent positions if they are empty.

We created three great features in this game, Player vs Player, Player vs Computer, and Computer vs Computer. For the Computer algorithm, we implement Minimax, where there are 3 levels, Easy where the depth is 2 , Medium with a depth of 4 and Hard with a depth of 6. The computer pieces are initially randomly placed.

_________________________________________________________________________________________

## How to use:

### To run the python code:
-Open a terminal or command prompt

-Navigate to the directory where "main.py" script is located using the cd command.

-Run the comand:
```python main.py```

_________________________________________________________________________________________

## Important Notes:

If Pygame is properly installed and configured, the script should run and your game should start. However, if Pygame is not installed or is not accessible, you may see an error message.
To install Pygame, you can use the following command:
```pip install game```

This will install the latest version of Pygame. 

_________________________________________________________________________________________

## Requirements

- Python (version 3.11.1)
- Pygame (version 1.9.6)

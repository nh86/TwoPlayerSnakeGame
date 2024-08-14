# Two Player Snake Game

Two Player Snake Game is a two-player version of the classic Snake game created using Python and the Pygame library. 

## Description

This is a 2D version, complete with graphics, of a two-player version of the classic Snake game built using Python and the Pygame library. Executing the main.py file starts the game and spawns two snakes onto the screen, with player one controlling their snake via the arrow keys and player two controlling their snake via the WASD keys on the same keyboard. 

Three apples continually spawn and the goal of the game is for both players to grow their snake by consuming apples. The game is won by one player forcing the other player to run into their snake or by forcing the other player to run into the walls of the game screen. Either action results is a victory for the opposing player. 

Ties can be had if the heads of each snake run into each other. 

## Usage

Start the game via running the main.py file.

## Attributions and Notes

The initial version of this game was built referencing Clear Code's Snake Game Tutorial; specifically, his usage of Vector2 class objects to store the body of the snake. 

The baseline game was expanded upon to incorporate a number of changes and upgrades, including adding a second snake, generating multiple fruits (as opposed to one), building in additional scoring and adding winner declarations for when a game ends. These changes also entailed significant modifications to the game code in order to account for new collision opportunities and the like.

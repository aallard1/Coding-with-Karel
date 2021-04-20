from karel.stanfordkarel import *

"""
File: PuzzleKarel.py
--------------------
Karel should finish the puzzle by picking up the last beeper (puzzle piece) and placing it in the right spot.
Karel should end in the same position Karel starts in -- the bottom left corner of the world.
"""

def main():
    """
    Karel finishes her puzzle by picking up the beeper, placing it in the puzzle, 
    then returning to her starting position. 
    """
    move_to_beeper()
    place_in_puzzle()
    return_to_start()

def move_to_beeper():
    if facing_east():
        move()
        move()
        pick_beeper()

def place_in_puzzle():
    if facing_east():
        move()
        turn_left()
        move()
        move()
        put_beeper()

def return_to_start():
    if facing_north():
        turn_around()
        move()
        move()
        turn_right()
        move()
        move()
        move()
        turn_around()

def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

if __name__ == '__main__':
    run_karel_program('Puzzle.w')
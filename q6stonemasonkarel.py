from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should be
able to solve the "repair the quad" problem from Assignment 1.
You should make sure that your program works for all of the
sample worlds supplied in the starter folder.
"""

def main():
    """
    Karel repairs a series of stone columns. Karel always starts on a column. 
    She climbs to the top of the first column, turns around and repairs as she goes, 
    returning to the bottom row. She then turns left (now facing east) and moves to the next column.
    She continues to repair columns, turn to face east, and move on until she finds a wall. 
    Then her task is complete.
    """
    first_column()
    move_to_next_column()
    check_for_column()
    move_to_next_column()
    check_for_column()
    move_to_next_column()
    check_for_column()

def first_column():
    turn_left()
    while front_is_clear():
        move()
    turn_around()
    while front_is_clear():
        place_column()
        move()
        if no_beepers_present():
            put_beeper()
    turn_left()

def move_to_next_column():
    for i in range(4):
        move()
    turn_left()

def check_for_column():
    while front_is_clear():
        if beepers_present():
            move()
            check_for_beepers()
        else:
            put_beeper()
    turn_around()
    if no_beepers_present():
        put_beeper()
    while front_is_clear():
        if beepers_present():
            move()
            check_for_beepers()
        else:
            move()            
    turn_left()

def turn_around():
    turn_left()
    turn_left()

def place_column():
    if no_beepers_present():
        put_beeper()

def check_for_beepers():
    if no_beepers_present():
        put_beeper()
        if front_is_clear():
            move()
            if no_beepers_present():
                put_beeper()

if __name__ == '__main__':
    run_karel_program('SampleQuad1.w')
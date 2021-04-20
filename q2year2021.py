from karel.stanfordkarel import *

"""
File: 2021.py
--------------------
When you finish writing this file, Karel should be able to place 20 beepers,
then 21 beepers, and end facing East to the right of the 21 beepers.
"""

def main():
    """
    Karel spells out 2021 in beepers by placing 20 beepers, moving, 
    placing 21 beepers, and then moving again.
    """
    place_20_beepers()
    place_21_beepers()

def place_20_beepers():
    for i in range(20):
        put_beeper()
    move()

def place_21_beepers():
    for i in range(21):
        put_beeper()
    move()

if __name__ == '__main__':
    run_karel_program('3x3.w')
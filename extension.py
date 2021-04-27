from karel.stanfordkarel import *

"""
File: ExtensionKarel.py
-----------------------
This file is for optional extension programs. 
"""

def main():
    """
    Karel draws the text, "HELLO WORLD". Works in Extension world 20*20.
    pre: Karel is facing east at (01, 01), prior to writing "HELLO WORLD".
    post: Karel is facing east at (20, 10), after writing "HELLO WORLD".
    """
    move_to_top_line()
    draw_h()
    move()
    draw_e()
    move()
    draw_l()
    move()
    draw_l()
    move()
    draw_o()
    move_down()
    draw_w()
    move()
    draw_o()
    move()
    draw_r()
    move()
    draw_l()
    move()
    draw_d()
    move()

""" 
pre: Karel is facing north, prior to writing.
post: Karel is facing east, one space past the completed letter H.
"""
def draw_h():
    turn_around()
    draw_line()
    turn_around()
    for i in range(2):
        move()
    turn_right()
    move()
    paint_corner(CYAN)
    move()
    turn_left()
    for i in range(2):
        move()
    turn_around()
    draw_line()
    turn_left()
    move()

""" 
pre: Karel is facing east, two spaces past the previous letter.
post: Karel is facing east, one space past the completed letter E.
"""
def draw_e():
    turn_left()
    draw_line()
    turn_right()
    draw_prong()
    for i in range(2):
        move()
    turn_left()
    draw_prong()
    for i in range(2):
        move()
    turn_left()
    draw_prong()
    turn_left()
    for i in range(3):
        move()

""" 
pre: Karel is facing east, two spaces past the previous letter.
post: Karel is facing east, one space past the completed letter L.
"""
def draw_l():
    turn_left()
    draw_line()
    turn_around()
    for i in range(4):
        move()
    turn_left()
    draw_prong()
    turn_left()
    for i in range(3):
        move()

""" 
pre: Karel is facing east, two spaces past the previous letter.
post: Karel is facing east, one space past the completed letter O. 
"""
def draw_o():
    turn_left()
    draw_line()
    turn_right()
    move()
    paint_corner(CYAN)
    move()
    turn_right()
    draw_line()
    turn_right()
    move()
    paint_corner(CYAN)
    move()
    turn_around()
    for i in range(3):
        move()

"""
pre: Karel is facing west.
post: Karel is facing east, one space past the completed letter W. 
"""
def draw_w():
    turn_right()
    draw_line()
    turn_around()
    for i in range(3):
        move()
    turn_left()
    move()
    paint_corner(CYAN)
    move()
    turn_right()
    move()
    turn_around()
    draw_line()
    turn_around()
    for i in range(4):
        move()
    turn_left()
    move()

"""
pre: Karel is facing east, two spaces past the previous letter.
post: Karel is facing east, one space past the completed letter R.
"""
def draw_r():
    turn_left()
    draw_line()
    turn_right()
    move()
    paint_corner(CYAN)
    move()
    turn_right()
    paint_corner(CYAN)
    move()
    paint_corner(CYAN)
    move()
    paint_corner(CYAN)
    turn_right()
    move()
    paint_corner(CYAN)
    move()
    turn_left()
    move()
    turn_left()
    move()
    paint_corner(CYAN)
    move()
    turn_right()
    move()
    paint_corner(CYAN)
    turn_left()
    move()

"""
pre: Karel is facing east, two spaces past the previous letter.
post: Karel is facing east, one space past the completed letter D.
"""
def draw_d():
    turn_left()
    draw_line()
    turn_right()
    move()
    paint_corner(CYAN)
    move()
    turn_right()
    move()
    for i in range(3):
        paint_corner(CYAN)
        move()
    turn_right()
    move()
    paint_corner(CYAN)
    move()
    turn_around()
    for i in range(2):
        move()

# Karel moves to 01, 20.
def move_to_top_line():
    turn_left()
    while front_is_clear():
        move()

""" 
pre: Karel is at the end of a 'line' of text, facing east.
post: Karel is at the beginning of the next 'line', facing west.
"""
def move_down():
    turn_right()
    for i in range(6):
        move()
    turn_right()
    while front_is_clear():
        move()
# Karel draws a line 5 spaces long.
def draw_line():
    for i in range(4):
        paint_corner(CYAN)
        move()
    paint_corner(CYAN)

# Karel draws a line 2 spaces long.
def draw_prong():
    move()
    paint_corner(CYAN)
    move()
    paint_corner(CYAN)
    turn_around()
    for i in range(2):
        move()
    turn_left()

# Karel turns right
def turn_right():
    for i in range(3):
        turn_left()

# Karel turns around
def turn_around():
    for i in range(2):
        turn_left()

if __name__ == "__main__":
    run_karel_program()
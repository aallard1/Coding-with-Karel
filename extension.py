from karel.stanfordkarel import *

"""
File: ExtensionKarel.py
-----------------------
This file is for optional extension programs. 
"""

def main():
    """
    Karel draws the text, "HELLO WORLD". Works in Extension world 20*20.
    pre: Karel has to be facing east at (01, 01), prior to writing "HELLO WORLD".
    post: Karel is facing east at (20, 10), after writing "HELLO WORLD".
    """
    move_to_top_line()
    draw_h()
    draw_e()
    draw_l()
    draw_l()
    draw_o()
    move_down()
    draw_w()
    draw_o()
    move()
    draw_r()
    draw_l()
    draw_d()

""" 
pre: Karel is facing north, prior to writing.
post: Karel is facing east, two spaces past the completed letter H.
"""
def draw_h():
    turn_south()
    draw_line_len5()
    turn_north()
    for i in range(2):
        move()
    turn_east()
    draw_line_len2()
    turn_north()
    draw_line_len2()
    turn_south()
    draw_line_len5()
    turn_east()
    for i in range(2):
        move()

""" 
pre: Karel is facing east, two spaces past the previous letter.
post: Karel is facing east, two spaces past the completed letter E.
"""
def draw_e():
    turn_north()
    draw_line_len5()
    turn_east()
    draw_line_len2()
    turn_west()
    for i in range(2):
        move()
    turn_south()
    for i in range(2):
        move()
    turn_east()
    draw_line_len2()
    turn_west()
    for i in range(2):
        move()
    turn_south()
    for i in range(2):
        move()
    turn_east()
    draw_line_len2()
    for i in range(2):
        move()

""" 
pre: Karel is facing east, two spaces past the previous letter.
post: Karel is facing east, two spaces past the completed letter L.
"""
def draw_l():
    turn_north()
    draw_line_len5()
    turn_south()
    for i in range(4):
        move()
    turn_east()
    draw_line_len2()
    for i in range(2):
        move()

""" 
pre: Karel is facing east, two spaces past the previous letter.
post: Karel is facing east, one space past the completed letter O. 
"""
def draw_o():
    turn_north()
    draw_line_len5()
    turn_east()
    draw_line_len2()
    turn_south()
    draw_line_len5()
    turn_west()
    draw_line_len2()
    turn_east()
    for i in range(3):
        move()

"""
pre: Karel is facing west.
post: Karel is facing east, two spaces past the completed letter W. 
"""
def draw_w():
    turn_north()
    draw_line_len5()
    turn_south()
    for i in range(3):
        move()
    turn_east()
    draw_line_len2()
    turn_south()
    move()
    turn_north()
    draw_line_len5()
    turn_south()
    for i in range(4):
        move()
    turn_east()
    for i in range(2):
        move()

"""
pre: Karel is facing east, two spaces past the previous letter.
post: Karel is facing east, two spaces past the completed letter R.
"""
def draw_r():
    turn_north()
    draw_line_len5()
    turn_east()
    draw_line_len2()
    turn_south()
    draw_line_len2()
    turn_west()
    draw_line_len2()
    turn_south()
    move()
    turn_east()
    move()
    paint_corner(CYAN)
    move()
    turn_south()
    move()
    paint_corner(CYAN)
    turn_east()
    for i in range(2):
        move()

"""
pre: Karel is facing east, two spaces past the previous letter.
post: Karel is facing east, one space past the completed letter D.
"""
def draw_d():
    turn_north()
    draw_line_len5()
    turn_east()
    draw_line_len1()
    move()
    turn_south()
    move()
    draw_line_len2()
    move()
    turn_west()
    move()
    draw_line_len1()
    turn_east()
    for i in range(3):
        move()

# Karel moves to 01, 20.
def move_to_top_line():
    turn_north()
    while front_is_clear():
        move()

""" 
pre: Karel is at the end of a 'line' of text, facing east.
post: Karel is at the beginning of the next 'line', facing west.
"""
def move_down():
    turn_south()
    for i in range(6):
        move()
    turn_west()
    while front_is_clear():
        move()

# Karel turns north.
def turn_north():
    while not_facing_north():
        turn_left()

# Karel turns east.
def turn_east():
    while not_facing_east():
        turn_left()

# Karel turns south.
def turn_south():
    while not_facing_south():
        turn_left()

# Karel turns west.
def turn_west():
    while not_facing_west():
        turn_left()

# Karel draws a line 5 spaces long.
def draw_line_len5():
    paint_corner(CYAN)
    for i in range(4):
        move()
        paint_corner(CYAN)

# Karel draws a line 3 spaces long.
def draw_line_len3():
    paint_corner(CYAN)
    for i in range(3):
        move()
        paint_corner(CYAN)

# Karel draws a line 2 spaces long.
def draw_line_len2():
    paint_corner(CYAN)
    for i in range(2):
        move()
        paint_corner(CYAN)

# Karel draws a line 1 space long.
def draw_line_len1():
    paint_corner(CYAN)
    for i in range(1):
        move()
        paint_corner(CYAN)

if __name__ == "__main__":
    run_karel_program()
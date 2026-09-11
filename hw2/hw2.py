''' 
hw2.py
Course: ECE 2210 - Python Programming for ECE
Semester: Fall 2026 
Name: Nick Troiano
CUID: C23493488
Known Bugs: None
'''

# You CANNOT import other modules
import math

'''
Function I:
Complete the following function called "cal_secs_ball_falling1".
A ball is dropped from a tower of height h (in meters) with initial velocity zero. 
Function "cal_secs_ball_falling1" takes the height of the tower as input and
RETURNS the time (in seconds) the ball takes until it hits the ground (ignoring air resistance). 
Refer to hw2.pdf for the kinematic formula.

Requirement(s):
    1) The return value is an integer that only keeps the integer part of the computed result.
''' 
def cal_secs_ball_falling1(h):
    g = 9.81 #m/s
    ## s = 0.5*g*(t**2)
    t = math.sqrt(2*h / g)
    return int(t)


'''
Function II:
Complete the following function called "cal_secs_ball_falling2":
A ball is AGAIN dropped from a tower of height h (in meters) with initial velocity zero. 
Function "cal_secs_ball_falling2" takes the height of the tower as input and
CALCULATES AND PRINTS the time (in seconds) the ball takes until it hits the ground, ignoring air resistance. 

Requirement(s):
    1) The displayed time is a floating-point number (i.e., no rounding needed).
    2) Function "cal_secs_ball_falling2" is a VOID function.
''' 
def cal_secs_ball_falling2(h):
    t = 0
    g = 9.81 #m/s
    ## s = 0.5*g*(t**2)
    t = math.sqrt(2*h / g)
    print(f"It takes {t} seconds for the ball to hit the ground.\n")


'''
Function III:
Complete the following function called "cal_altitude" that 
calculates and returns the needed altitude h (in meters) above the earth’s surface that 
the satellite must have so that it orbits the planet once every t minutes.
Refer to HW2.pdf for the formula used to calculate the altitude.

Hint: The parameter t is in minutes and T in the given formula is in seconds! 
'''
def cal_altitude(t):
    G = 6.67 * (10**-11)
    M = 5.97 * (10**24)
    R = 6371 * (10**3)
    T = t*60

    h = (((G*M*(T**2))/(4*(math.pi**2)))**(1/3))-R
    return h


'''
Function IV:
Complete the following function called "draw_grid" that draws a grid 
like the one shown in "HW2.pdf", which is only composed of ‘+’, ‘-’, ‘|’ and ‘ ’ (space).
Hint: Consider using string addition (concatenation) and multiplication (repetition).
'''
def draw_grid():
    dash = '- '
    plus = '+ '
    vertical = '| '
    space = '  '
    junction_line = plus + dash*4 + plus + dash*4 + plus[0] + '\n'
    other_line = vertical + space*4 + vertical + space*4 + vertical[0] + '\n'
    out = junction_line + other_line*4 + junction_line + other_line*4 + junction_line.strip('\n')
    print(out)

# Function Calls:
# Do NOT modify the code below!!!
if __name__ == '__main__':
    try:
        print(
            f"It takes {cal_secs_ball_falling1(100)} "
            f"seconds for the ball to hit the ground.\n"
        )
    except Exception as e:
        print(f"[Error in cal_secs_ball_falling1]: {e}\n")
    
    try:
        cal_secs_ball_falling2(100)
    except Exception as e:
        print(f"[Error in cal_secs_ball_falling2]: {e}\n")
    
    try:
        print(cal_altitude(90), '\n')
    except Exception as e:
        print(f"[Error in cal_altitude]: {e}\n")
    
    try:
        print(cal_altitude(45), '\n')
    except Exception as e:
        print(f"[Error in cal_altitude]: {e}\n")

    try:
        draw_grid()
    except Exception as e:
        print(f"[Error in draw_grid]: {e}\n")

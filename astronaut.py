from math import sin

def animate_astronaut(screen, f):
    headY1 = 50 * sin(0.05 * f) + 200  # Vertical oscillation for astronaut's Y position

    arm1 = screen.create_polygon(412, headY1+65, 417, headY1+90, 365, headY1+130, 360, headY1+110, fill="white", outline="black")
    arm2 = screen.create_polygon(490, headY1+65, 485, headY1+90, 537, headY1+130, 542, headY1+110, fill="white", outline="black")
    tank = screen.create_polygon(395, headY1+40, 505, headY1+40, 490, headY1+85, 411, headY1+85, fill="#C5C6D0")
    body = screen.create_rectangle(409, headY1+65, 

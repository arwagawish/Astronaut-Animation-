from tkinter import *
from time import sleep
from stars import create_stars, animate_stars, delete_stars
from meteors import create_meteors, animate_meteors, delete_meteors
from planets import create_planets, animate_planets, delete_planets
from astronaut import animate_astronaut

root = Tk()
screen = Canvas(root, width=1000, height=1000, background="black")
screen.pack()

# Create the stars, meteors, and planets
stars = create_stars(900)
meteors = create_meteors(5)
planets = create_planets(4)

# Animation loop
for f in range(10000):
    animate_stars(screen, stars)
    animate_meteors(screen, meteors)
    animate_planets(screen, planets)
    animate_astronaut(screen, f)

    screen.update()
    sleep(0.03)
    
    delete_stars(screen, stars)
    delete_meteors(screen, meteors)
    delete_planets(screen, planets)

root.mainloop()

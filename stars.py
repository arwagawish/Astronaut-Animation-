from random import randint

def create_stars(num_stars):
    starX, starY, xSpeed, size, starDrawings = [], [], [], [], []
    for i in range(num_stars):
        starX.append(randint(0, 1000))
        starY.append(randint(0, 1000))
        xSpeed.append(randint(-10, 10))
        size.append(randint(0, 5))
        starDrawings.append(0)
    return starX, starY, xSpeed, size, starDrawings

def animate_stars(screen, stars):
    starX, starY, xSpeed, size, starDrawings = stars
    for i in range(len(starX)):
        starDrawings[i] = screen.create_oval(starX[i], starY[i], starX[i] + size[i], starY[i] + size[i], fill="white")
        starX[i] += xSpeed[i]

        if starX[i] <= 0 or starX[i] >= 1000:
            xSpeed[i] *= -1

def delete_stars(screen, stars):
    _, _, _, _, starDrawings = stars
    for i in range(len(starDrawings)):
        screen.delete(starDrawings[i])

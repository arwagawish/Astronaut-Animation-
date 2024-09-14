from random import randint, choice

def create_meteors(num_meteors):
    meteorX, meteorY, meteorX2, meteorY2 = [], [], [], []
    meteorX3, meteorY3, meteorX4, meteorY4 = [], [], [], []
    meteorXspeed, meteorColour, meteorSize, meteorDrawing = [], [], [], []
    
    for i in range(num_meteors):
        meteorX.append(randint(0, 1000))
        meteorY.append(randint(0, 1000))
        meteorX2.append(randint(10, 50))
        meteorY2.append(randint(30, 70))
        meteorX3.append(randint(20, 50))
        meteorY3.append(randint(60, 80))
        meteorX4.append(randint(80, 90))
        meteorY4.append(randint(2, 50))
        meteorXspeed.append(randint(-25, 25))
        meteorColour.append(choice(["#696880", "#41424C", "#787276", "#59515E"]))
        meteorSize.append(randint(10, 30))
        meteorDrawing.append(0)

    return meteorX, meteorY, meteorX2, meteorY2, meteorX3, meteorY3, meteorX4, meteorY4, meteorXspeed, meteorColour, meteorSize, meteorDrawing

def animate_meteors(screen, meteors):
    (meteorX, meteorY, meteorX2, meteorY2, meteorX3, meteorY3, meteorX4, meteorY4, meteorXspeed, meteorColour, meteorSize, meteorDrawing) = meteors
    for i in range(len(meteorX)):
        meteorDrawing[i] = screen.create_polygon(
            meteorX[i], meteorY[i], meteorX[i]+meteorX2[i], meteorY[i]+meteorY2[i], 
            meteorX[i]+meteorX3[i], meteorY[i]+meteorY3[i], meteorX[i]+meteorX4[i], meteorY[i]+meteorY4[i], 
            fill=str(meteorColour[i])
        )
        meteorX[i] += meteorXspeed[i]

        if meteorX[i] <= -100 or meteorX[i] >= 1100:
            meteorXspeed[i] *= -1

def delete_meteors(screen, meteors):
    _, _, _, _, _, _, _, _, _, _, _, meteorDrawing = meteors
    for i in range(len(meteorDrawing)):
        screen.delete(meteorDrawing[i])

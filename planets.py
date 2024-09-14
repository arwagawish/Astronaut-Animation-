from random import randint, choice

planetColour1 = ["#BE5504", "#311465", "#0A1172", "#234F1E"]
planetColour2 = ["#ED7014", "#592693", "#1520A6", "#466D1D"]
planetColour3 = ["#FCAE1E", "#B47EE5", "#3944BC", "#98BF64"]
planetColour4 = ["#F9E076", "#E39FF6", "#63C5DA", "#AEF359"]

def create_planets(num_planets):
    planetX, planetY, planetXspeed, planetSize = [], [], [], []
    planetDrawing1, planetDrawing2, planetDrawing3, planetDrawing4 = [], [], [], []

    for i in range(num_planets):
        planetX.append(randint(0, 1000))
        planetY.append(randint(0, 700))
        planetXspeed.append(5 * choice([1, -1]))
        planetSize.append(randint(100, 300))
        planetDrawing1.append(0)
        planetDrawing2.append(0)
        planetDrawing3.append(0)
        planetDrawing4.append(0)

    return planetX, planetY, planetXspeed, planetSize, planetDrawing1, planetDrawing2, planetDrawing3, planetDrawing4

def animate_planets(screen, planets):
    planetX, planetY, planetXspeed, planetSize, planetDrawing1, planetDrawing2, planetDrawing3, planetDrawing4 = planets
    for i in range(len(planetX)):
        planetDrawing1[i] = screen.create_oval(planetX[i], planetY[i], planetX[i] + planetSize[i], planetY[i] + planetSize[i], fill=str(planetColour1[i]))
        planetDrawing2[i] = screen.create_oval(planetX[i]+20, planetY[i]+20, planetX[i]+planetSize[i]-20, planetY[i]+planetSize[i]-20, fill=str(planetColour2[i]))
        planetDrawing3[i] = screen.create_oval(planetX[i]+40, planetY[i]+40, planetX[i]+planetSize[i]-40, planetY[i]+planetSize[i]-40, fill=str(planetColour3[i]))
        planetDrawing4[i] = screen.create_oval(planetX[i]+60, planetY[i]+60, planetX[i]+planetSize[i]-60, planetY[i]+planetSize[i]-60, fill=str(planetColour4[i]))
        planetX[i] += planetXspeed[i]

        if planetX[i] + planetSize[i] <= -100 or planetX[i] + planetSize[i] >= 1500:
            planetXspeed[i] *= -1

def delete_planets(screen, planets):
    _, _, _, _, planetDrawing1, planetDrawing2, planetDrawing3, planetDrawing4 = planets
    for i in range(len(planetDrawing1)):
        screen.delete(planetDrawing1[i], planetDrawing2[i], planetDrawing3[i], planetDrawing4[i])

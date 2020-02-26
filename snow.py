import matplotlib.pyplot as plt
import numpy

width = 50
length = 100
depth = .75

uk = .3

xarr = [0, 0.01, 0.02, 0.03]
xarr = [i*5280 for i in xarr]
print(xarr)
altarr = [4868, 4845, 4812, 4775]

plt.plot(xarr, altarr)

def computeSlope(dx, dy):
    print("dx: " + str(dx) + "  dy: " + str(dy))
    tan = dy/dx
    print(tan)
    slope = (numpy.arctan(tan))
    return (slope * -1)

slopearr = [computeSlope(xarr[i] - xarr[i + 1], altarr[i] - altarr[i + 1]) for i in range(0, 3)]
print(slopearr)

lenarr = [0, 0, 0]
for i in range(0, 3):
    lenarr[i] = numpy.sqrt((xarr[i] - xarr[i+1])**2 + (altarr[i] - altarr[i+1])**2 )
print(lenarr)

m = width*depth*length*450
Fg = m*9.8

for i in range(0,3):
    F1 = Fg * numpy.cos(slopearr[i])
    Fn = Fg * numpy.sin(slopearr[i])
    Ffk = uk * Fn
    Fnet = F1 - Ffk
    a = Fnet/m
    len = lenarr[i] * 0.3048
    dt = numpy.sqrt(len*2/a)
    vf = a*dt
    print("dt: " + str(dt) + " vf: " +str(vf))

plt.show()
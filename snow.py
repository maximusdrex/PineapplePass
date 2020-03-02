import matplotlib.pyplot as plt
import numpy

width = 50
length = 100
depth = .75

uk = .3

xarr = [0, 0.01, 0.02, 0.03]
xarr = [i*1609.34 for i in xarr]
#convert to meters
print("x: " + str(xarr))
altarr = [4868, 4845, 4812, 4775]
#convert to meters
altarr = [i*0.3048 for i in altarr]
print("altitudes: " + str(altarr))

if(len(xarr) != len(altarr)):
    print("error! \n Lengths of x array and altitude array do not match")
    exit()

# plt.plot(xarr, altarr)

dxarr = [xarr[i+1] - xarr[i] for i in range(0, len(xarr) - 1)]
dyarr = [(altarr[i+1] - altarr[i]) * -1 for i in range(0, len(altarr) - 1)]
print("dx: " + str(dxarr))
print("dy: " + str(dyarr))


def computeSlope(dx, dy):
    tan = dy/dx
    slope = (numpy.arctan(tan))
    return (slope)

slopearr = [computeSlope(dxarr[i], dyarr[i]) for i in range(len(dxarr))]
print("slopes: " + str(slopearr))

lenarr = [0, 0, 0]
for i in range(0, 3):
    lenarr[i] = numpy.sqrt((xarr[i] - xarr[i+1])**2 + (altarr[i] - altarr[i+1])**2 )
print(lenarr)

m = width*depth*length*450
Fg = m*9.8

times = [0]

for i in range(0,len(slopearr)):
    F1 = Fg * numpy.cos(slopearr[i])
    Fn = Fg * numpy.sin(slopearr[i])
    Ffk = uk * Fn
    Fnet = F1 - Ffk
    a = Fnet/m
    len = lenarr[i] * 0.3048
    dt = numpy.sqrt(len*2/a)
    times.append(times[i] + dt)
    vf = a*dt
    print("dt: " + str(dt) + " vf: " +str(vf))

plt.plot(times, altarr)
plt.show()
import seaborn as sns
import matplotlib.pyplot as plt
import numpy

width = 50
length = 100
depth = .75


feetToMeters = lambda x : x * 0.3048
mileToMeters = lambda x : x * 1609.34


xarr = [0, 0.01, 0.02, 0.03, 0.04, 0.05]
xarr = [mileToMeters(i) for i in xarr]
#convert to meters
print("x: " + str(xarr))
altarr = [4868, 4845, 4812, 4775, 4735, 4685]
#convert to meters
altarr = [feetToMeters(i) for i in altarr]
print("altitudes: " + str(altarr))


#error if data is improperly formatted
if(len(xarr) != len(altarr)):
    print("error! \n Lengths of x array and altitude array do not match")
    exit()

# plt.plot(xarr, altarr)


#differences at each point
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

lenarr = []
for i in range(0, len(xarr) - 1):
    lenarr.append(numpy.sqrt((xarr[i] - xarr[i+1])**2 + (altarr[i] - altarr[i+1])**2 ))
print(lenarr)

m = width*depth*length*450
Fg = m*9.8

def simulate(uk):
    times = [0]
    velarr = []
    for i in range(0,len(slopearr)):
        vi = 0
        if (i != 0):
            vi = velarr[i-1]
        F1 = Fg * numpy.cos(slopearr[i])
        Fn = Fg * numpy.sin(slopearr[i])
        Ffk = uk * Fn
        Fnet = F1 - Ffk
        a = Fnet/m
        len = lenarr[i] * 0.3048
        dt = numpy.sqrt(len*2/a)
        times.append(times[i] + dt)
        vf = a*dt + vi
        velarr.append(vf)
        print("x: " + str(xarr[i + 1]) + " vf: " +str(vf))

    return velarr


xplotarr = xarr
xplotarr.remove(xplotarr[0])

sns.lineplot(x=xplotarr, y=simulate(0))
plt.show()
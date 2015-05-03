from pylab import *
from numpy import exp
from mpl_toolkits.mplot3d import Axes3D

EULAR_EXP_INTE = 0
EULAR_IMP_INTE = 1

def func_eei(dt, x, y):
	return (-dt*x*y+x, -dt*y+y)

def func_heun(dt, x, y):
	x_tilde = x - x * y *dt
	y_tilde = y - y * dt
	return (x+(dt/2)*(-x_tilde*y_tilde-x*y), y+(dt/2)*(-y_tilde-y))

def func_anloe(t, x, y):
	return (exp(exp(-t))/exp(1),exp(-t))

def ei(x0, y0, t_start, t_end, t_nump):
	y = y0
	x = x0
	dt=(float)(t_start+t_end)/(float)(t_nump)
	for t in range(t_nump) :
		yield x,y
		x,y = func_eei(dt, x, y)

def heun(x0, y0, t_start, t_end, t_nump):
	y = y0
	x = x0
	dt=(float)(t_start+t_end)/(float)(t_nump)
	for t in range(t_nump) :
		yield x,y
		x,y = func_heun(dt, x, y)

def anloe(x0, y0, t_start, t_end, t_nump):
	y = y0
	x = x0
	for i in range(t_nump):
		yield x,y
		t = (float)(i) * ((float)(t_end - t_start) / (float)(t_nump)) + (float)(t_start)
		x,y = func_anloe(t, x, y)

fig = figure()
ax = fig.gca(projection = '3d')
t_start = 0
t_end = 10
t_nump = 100000

y_start = 0
y_end = 10
x_start = 0
x_end = 10

t = np.linspace(t_start, t_end, t_nump, endpoint=True)
x0 = 1
y0 = 1
x = []
y = []

for xt, yt in ei(x0, y0, t_start, t_end, t_nump):
	x.append(xt)
	y.append(yt)
ax.plot(x, y, t, color = 'blue', linestyle = '-', label = 'eular explizite Intergration')

x = []
y = []
for xt, yt in heun(x0, y0, t_start, t_end, t_nump):
	x.append(xt)
	y.append(yt)
ax.plot(x, y, t, color = 'green', linestyle = '-', label = 'heun Verfahren')

x = []
y = []
for xt, yt in anloe(x0, y0, t_start, t_end, t_nump):
	x.append(xt)
	y.append(yt)
ax.plot(x, y, t, color = 'red', linestyle = '-', label = 'analytische Loesung')

title('Vergleichung von zweidimensionalen DGL1 with x0 = 1, y0 = 1')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('t')
legend(loc = 'lower right')
show()
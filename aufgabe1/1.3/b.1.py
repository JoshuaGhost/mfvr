from pylab import *
from numpy import exp
from mpl_toolkits.mplot3d import Axes3D

EULAR_EXP_INTE = 0
EULAR_IMP_INTE = 1

def func_eei(dt, x, y):
	return (-dt*x*y+x, -dt*y+y)

def func_anloe(t, x, y):
	return (exp(exp(-t))/exp(1),exp(-t))

def ei(x0, y0, t_start, t_end, t_nump, method):
	y = y0
	x = x0
	dt=(float)(t_start+t_end)/(float)(t_nump)
	for t in range(t_nump) :
		yield x,y
		x,y = func_eei(dt, x, y)

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
x_ei=[]
y_ei=[]
x_anloe = []
y_anloe = []
for xt, yt in ei(x0, y0, t_start, t_end, t_nump, EULAR_EXP_INTE):
	x_ei.append(xt)
	y_ei.append(yt)
for xt, yt in anloe(x0, y0, t_start, t_end, t_nump):
	x_anloe.append(xt)
	y_anloe.append(yt)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('t')
title('Vergleichung von zweidimensionalen DGL1 with x0 = 1, y0 = 1')
ax.plot(x_ei, y_ei, t, color = 'blue', linestyle = '-', label = 'eular explizite Intergration')
ax.plot(x_anloe, y_anloe, t, color = 'red', linestyle = '-', label = 'analytische Loesung')
legend(loc = 'lower right')
show()
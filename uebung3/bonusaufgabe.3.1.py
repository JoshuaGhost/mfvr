from pylab import *
from numpy import exp, log

alpha = 4.0
beta  = 0.05
delta = 0.07
gamma = 30.0

t_start = 0
t_end = 3
t_nump = 10000

x0 = 71.0

def deg(x, y):
	xnew = alpha*x - beta*x*y
	ynew = delta*x*y - gamma*y
	return xnew, ynew
	
def func_heun(dt, x, y):
	xe, ye = deg(x, y)
	xt = x + xe*dt
	yt = y + ye*dt
	
	xh, yh = deg(xt, yt)
	xh = x + dt/2*(xe + xh)
	yh = y + dt/2*(ye + yh)
	return (xh, yh)

def heun(x0, y0, t_start, t_end, t_nump):
	x = x0
	y = y0
	dt=(float)(t_start+t_end)/(float)(t_nump)
	for t in range(t_nump) :
		yield x, y
		x,y = func_heun(dt, x, y)

def get_y0(x, v):
	v = v+delta*x-gamma*log(x)
	y0 = 100.0
	while 1:
		y1 = y0-(-beta*y0+alpha*log(y0)-v)/(-beta+alpha/y0)
		if abs(y1 - y0)<0.000001:
			return y1
		y0 = y1

t = np.linspace(t_start, t_end, t_nump, endpoint=True)
v_array = [1, 5, 10, 15, 80]
color_array = ['b', 'g', 'r', 'c', 'y']
for i, v in enumerate(v_array):
	x = []
	y = []
	y0 = get_y0(x0, v)
	for xt, yt in heun(x0, y0, t_start, t_end, t_nump):
		x.append(xt)
		y.append(yt)
	plot(x, y, color = color_array[i], label = 'V = %d' %v)

title('Phase Space Plot (where V=-delta*x+gamma*ln(x)-beta*y+alpha*ln(y))')
xlabel('Number of Prey')
ylabel('Number of Predators')
legend()
show()
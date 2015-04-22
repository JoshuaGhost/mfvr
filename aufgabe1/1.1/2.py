from pylab import *

def func2(dx, y):
	return dx*y*y+y

def eei(y0, x_start, x_end, x_nump):
	y = y0
	dx=(float)(x_start+x_end)/(float)(x_nump)
	for x in range(x_nump) :
		yield y
		y = func2(dx, y)

x_start = 0
x_end = 10
x_nump = 10000
y_start = -10
y_end = 10

x = np.linspace(x_start, x_end, x_nump, endpoint=True)

y0_start = -1
y0_end = 1
stepy0 = 20
for i in range((int)((y0_end-y0_start)*stepy0+1)):
	y0 =(float)(i)/(float)(stepy0)+(float)(y0_start)
	y = [yt for yt in eei(y0, x_start, x_end, x_nump)]
	plot(x,y)
ylim(y_start, y_end)
show()
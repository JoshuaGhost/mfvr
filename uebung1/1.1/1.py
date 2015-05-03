from pylab import *

def func1(dx, y):
	return dx-2*y*dx+y
	
def eei(y0, x_start, x_end, x_nump):
	y = y0
	dx=(float)(x_start+x_end)/(float)(x_nump)
	for x in range(x_nump) :
		yield y
		y = func1(dx, y)

x_start = 0
x_end = 10
x_nump = 100
y_start = 0
y_end = 1000

x = np.linspace(x_start, x_end, x_nump, endpoint=True)

y0_start = 0
y0_end = 10
stepy0 = 1
for i in range((y0_end-y0_start)*stepy0+1):
	y0 =(float)(i)/(float)(stepy0)+(float)(y0_start)
	y = [yt for yt in eei(y0, x_start, x_end, x_nump)]
	plot(x,y)
#ylim(y_start, y_end)
show()
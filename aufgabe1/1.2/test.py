from pylab import *

EULAR_EXP_INTE = 0
EULAR_IMP_INTE = 1

def funct_eii(dx, y):
	return y/(1-dx)

def funct_eei(dx, y):
	return dx*y+y

def ei(y0, x_start, x_end, x_nump, method):
	y = y0
	dx=(float)(x_start+x_end)/(float)(x_nump)
	for x in range(x_nump) :
		yield y
		if method == EULAR_EXP_INTE:
			y = funct_eei(dx, y)
		else:
			y = funct_eii(dx, y)

x_start = 0
x_end = 10
x_nump = 1000
y_start = 0
y_end = 1000

x = np.linspace(x_start, x_end, x_nump, endpoint=True)

y0_start = 1
y0_end = 1
stepy0 = 1
for i in range((y0_end-y0_start)*stepy0+1):
	y0 =(float)(i)/(float)(stepy0)+(float)(y0_start)
	y = [yt for yt in ei(y0, x_start, x_end, x_nump, EULAR_EXP_INTE)]
	plot(x, y, color = 'blue', linestyle = '-', label = 'eular explizite Intergration')
	y = [yt for yt in ei(y0, x_start, x_end, x_nump, EULAR_IMP_INTE)]
	plot(x, y, color = 'red', linestyle = '-', label = 'eular implizite Intergration')
#ylim(y_start, y_end)
legend(loc = 'upper left')
title('comparition of y\'=y when y0 = 1')
show()
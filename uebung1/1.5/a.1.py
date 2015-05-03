from pylab import *

class Ex_Intprt(object):
	"""Ex_Intprt, euler explicit integration of y'=ky"""
	
	def __init__(self, x_start = 0, x_end = 10, p_num = 1000, k = 1):
		self.p_num = p_num
		self.x = np.linspace(x_start, x_end, p_num, endpoint=True)
		self.dx=(float)(x_start+x_end)/(float)(p_num)
		self.k = k
		if (1+self.dx*k<1 and 1+self.dx*k>-1):
			self.isastable = True
		else:
			self.isastable = False

	def funct_eei(self, y):
		return self.dx*self.k*y+y

	def ei(self, y0):
		y = y0
		for x in range(self.p_num):
			yield y
			y = self.funct_eei(y)

	def gen_y(self, y0_start = 1, y0_end = 1, y0_step = 1):
		self.y0_start = y0_start
		self.y0_end   = y0_end
		self.y0_step  = y0_step
		for i in range((self.y0_end-self.y0_start)*self.y0_step+1):
			y0 =(float)(i)/(float)(y0_step)+(float)(y0_start)
			self.y = [yt for yt in self.ei(y0)]


exi1 = Ex_Intprt(x_start = 0, x_end = 10, p_num = 40, k = -0.5)
exi1.gen_y(y0_start = 1, y0_end = 1, y0_step = 1)

exi2 = Ex_Intprt(x_start = 0, x_end = 10, p_num = 40, k = -30)
exi2.gen_y(y0_start = 1, y0_end = 1, y0_step = 1)

sca(subplot(1,2,1))
plot(exi1.x, exi1.y, color = 'blue', linestyle = '-')
if exi1.isastable:
	negation = ''
else:
	negation = 'n\'t'
title('y\'=ky where y0 = 1, k=%.2f, dx=%.2f which is%s A-stable' % 
	  (exi1.k, exi1.dx, negation))

sca(subplot(1,2,2))
plot(exi2.x, exi2.y, color = 'red', linestyle = '-')
if exi2.isastable:
	negation = ''
else:
	negation = 'n\'t'
title('y\'=ky where y0 = 1, k=%.2f, dx=%.2f which is%s A-stable' % 
	  (exi2.k, exi2.dx, negation))

show()
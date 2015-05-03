from pylab import *

EULER_EXPLIZITE_INTG = 0
EULER_IMPLIZITE_INTG = 1

class Euler_Intg(object):
	
	def __init__(self, x_start = 0, x_end = 10, p_num = 1000, k = 1):
		self.p_num = p_num
		self.x = np.linspace(x_start, x_end, p_num, endpoint=True)
		self.dx=(float)(x_start+x_end)/(float)(p_num)
		self.k = k
		self.isastable = True
		
	def intg(self, y0):
		pass

	def gen_y(self, y0_start = 0.5, y0_end = 0.5, y0_step = 1):
		self.y0_start = y0_start
		self.y0_end   = y0_end
		self.y0_step  = y0_step
		for i in range(int((self.y0_end-self.y0_start)*self.y0_step+1)):
			y0 =(float)(i)/(float)(y0_step)+(float)(y0_start)
			self.y = [yt for yt in self.intg(y0)]

	def astable_test(self, ynew, ynow):
		if abs(ynew)>=abs(ynow):
			return False
		else:
			return True
			
class Euler_Expl_Intg(Euler_Intg):

	def __init__(self, x_start = 0, x_end = 10, p_num = 1000, k = 1):
		super(Euler_Expl_Intg, self).__init__(x_start, x_end, p_num, k)

	def funct_eei(self, y):
		ret = 3*y*(1-y)
		self.isastable = self.astable_test(ret, y)
		return ret

	def intg(self, y0):
		y = y0
		for x in range(self.p_num):
			yield y
			y = self.funct_eei(y)

class Euler_Impl_Intg(Euler_Intg):
	
	def __init__(self, x_start = 0, x_end = 10, p_num = 1000, k = 1):
		super(Euler_Impl_Intg, self).__init__(x_start, x_end, p_num, k)
		
	def funct_eii(self, y):
		ret = y/(1.0-self.dx*self.k)
		self.isastable = self.astable_test(ret, y)
		return ret

	def intg(self, y0):
		y = y0
		for x in range(self.p_num):
			yield y
			y = self.funct_eii(y)

print 'Euler explicit and implicit integration of y\'=-ky'
k = float(raw_input('Please input k:'))

eei = Euler_Expl_Intg(x_start = 0, x_end = 10, p_num = 404, k = -k)
eei.gen_y(y0_start = 0.5, y0_end = 0.5, y0_step = 1)

eii = Euler_Impl_Intg(x_start = 0, x_end = 10, p_num = 404, k = -k)
eii.gen_y(y0_start = 1, y0_end = 1, y0_step = 1)

print eei.y

sca(subplot(1,2,1))
plot(eei.x, eei.y, color = 'blue', linestyle = '-')
negation = '' if eei.isastable else 'n\'t'
title('eular explizite integration which is%s A-stable' % 
	  negation)

sca(subplot(1,2,2))
plot(eii.x, eii.y, color = 'red', linestyle = '-')
negation = '' if eii.isastable else 'n\'t'
title('eular implizite intepretor which is%s A-stable' % 
	  negation)

show()
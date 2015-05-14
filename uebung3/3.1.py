from pylab import *
from numpy import exp

alpha = 0.0075
beta  = 0.0055
xi    = 0.09
delta = 0.0001
rho   = 0.005
c     = 0.00075

t_start = 0
t_end = 1000
t_nump = 100000

s0 = 500.0

def deg(s, i, z, r):
	snew = -beta*s*z + c*z - delta*s
	inew = beta*s*z - rho*i - delta*i
	znew = rho*i + xi*r - alpha*s*z - c*z
	rnew = alpha*s*z - xi*r + delta*s + delta*i
	return snew, inew, znew, rnew
	
def func_heun(dt, s, i, z, r):
	se, ie, ze, re = deg(s, i, z, r)
	st = s + se*dt
	it = i + se*dt
	zt = z + ze*dt
	rt = r + re*dt
	sh, ih, zh, rh = deg(st, it, zt, rt)
	sh = s + dt/2*(se + sh)
	ih = i + dt/2*(ie + ih)
	zh = z + dt/2*(ze + zh)
	rh = r + dt/2*(re + rh)
	return (sh, ih, zh, rh)

def heun(s0, t_start, t_end, t_nump):
	s = s0
	i = 0
	z = 0
	r = 0
	dt=(float)(t_start+t_end)/(float)(t_nump)
	for t in range(t_nump) :
		yield s+i, z
		s, i, z, r = func_heun(dt, s, i, z, r)
		
t = np.linspace(t_start, t_end, t_nump, endpoint=True)
s = []
z = []

for st, zt in heun(s0, t_start, t_end, t_nump):
	s.append(st)
	z.append(zt)

plot(t, s, color = 'blue', label = 'Suscepties')
plot(t, z, color = 'red',  label = 'Zombie')

title('Model with Treatment')
xlabel('time')
ylabel('Population Values')
legend()
show()
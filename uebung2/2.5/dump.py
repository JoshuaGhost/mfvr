import math
from numpy import array, dot, sqrt, eye, ones
import json

dt = 0.001
step = 5
zero = math.sqrt(2.0/5.0)/float(step)
distance = 0.7 * zero
radius = 200
gravity = 3000.0
time = 1000
mass = 1

def half_circle(radius):
	center = Cordnt(0.0, 0.0)
	for x in range(-radius, radius):
		yield float(x), 0.0
	for y in range(step, radius+step, step):
		for x in range(-radius, radius+step, step):
			if Cordnt.eucl_dist(Cordnt(float(x), float(y)), center) <= radius:
				yield float(x),float(y)

class Cordnt(object):

	def __init__(self, x0 = 0, y0 = 0):
		self.x = float(x0)
		self.y = float(y0)

	def eucl_dist(c1, c2):
		return float(math.sqrt(float(c1.x-c2.x)**2+
					float(c1.y-c2.y)**2))

class Waterdrop(object):

	def __init__(self, radius, gravity, mass = 1):
		self.mass = mass
		self.radius = radius
		self.gravity = gravity

		self.px = []
		self.py = []
		self.deck = []
		self.deckx = []
		for x,y in half_circle(radius):
			self.px.append(float(x))
			self.py.append(float(y))
			if y == 0.0:
				self.deck.append(len(self.py)-1)
				self.deckx.append(x)

		self.num = len(self.px)
		self.gain = [[1.0]*self.num]*self.num
		for d in self.deck:
			self.gain[d] = [1.75]*self.num
		self.gain = array(self.gain).transpose()
		self.px = array([self.px]).transpose()
		self.py = array([self.py]).transpose()

		self.vx = array([[0.0]]*self.num)
		self.vy = self.vx.copy()

	def step(self, time):
		for i in range(time):
			yield self.px, self.py

			num = self.num
			xsub = dot(array([[1.0]]*num), self.px.transpose())-\
					dot(self.px, array([[1.0]*num]))
				   
			ysub = dot(array([[1.0]]*num), self.py.transpose())-\
					dot(self.py, array([[1.0]*num]))
			
			r = sqrt((xsub)**2 + (ysub)**2)+eye(num)
			
			r = r*distance
			f = 20.0/r**3-8.0/r**5
			for i in range(num):
				f[i][i] = 0.0

			#f = f*self.gain*20
			f = f*self.gain

			ax = dot(f*(xsub/r)/self.mass, [[1.0]]*num)
			ay = dot(f*(ysub/r)/self.mass, [[1.0]]*num) + array([[self.gravity]]*num)

			self.vx = self.vx + ax*dt
			self.vy = self.vy + ay*dt

			self.px = self.px + self.vx*dt
			self.py = self.py + self.vy*dt

			for i, d in enumerate(self.deck):
				self.py[d] = 0
				self.px[d] = self.deckx[i]

wd = Waterdrop(radius, gravity, mass)
xs = []
ys = []
for x, y in wd.step(time):
	xs.append(map(int, x.transpose()[0].tolist()))
	ys.append(map(int, y.transpose()[0].tolist()))


with open("dumpx.new.json", "w") as df:
	json.dump(xs, df)
with open("dumpy.new.json", "w") as df:
	json.dump(ys, df)
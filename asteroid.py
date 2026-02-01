# asteroid.py
#
# (c) ClicKill Microbits
import random
from circleshape import *
from constants import LINE_WIDTH,ASTEROID_MIN_RADIUS
from logger import log_event

# Base class for Asteroid objects
class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)
		# print("An Asteroid was instantiated")

	def __repr__(self):
		return f"Asteroid: position={self.position}, radius={self.radius}"

	def split(self):
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			return
		else:
			log_event("asteroid_split")
			random_angle = random.uniform(20, 50)
			new_vel1 = self.velocity.rotate(random_angle)
			new_vel1 *= 1.5
			new_vel2 = self.velocity.rotate(-random_angle)
			new_vel2 *= 1.5
			new_radius = self.radius - ASTEROID_MIN_RADIUS
			new_as1 = Asteroid(self.position.x, self.position.y, new_radius)
			new_as1.velocity = new_vel1
			new_as2 = Asteroid(self.position.x, self.position.y, new_radius)
			new_as2.velocity = new_vel2

	def draw(self, screen):
		# overridden
		# print(f"{self}")
		pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

	def update(self, dt):
		# overridden
		# print("self.update() called")
		self.position += self.velocity * dt


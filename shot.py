# shot.py
#
#  (c) ClicKill Microbits
from circleshape import *
from constants import LINE_WIDTH,SHOT_RADIUS

class Shot(CircleShape):
	def __init__(self, x, y):
		super().__init__(x, y, SHOT_RADIUS)

	def __repr__(self):
		return f"Shot: position={self.position}, radius={self.radius}"

	def draw(self, screen):
		# overridden
		# print(f"{self}")
		pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

	def update(self, dt):
		# overridden
		# print("self.update() called")
		self.position += self.velocity * dt


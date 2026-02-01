# player.py
#
# (c) ClicKill Microbits
from circleshape import *
from constants import PLAYER_RADIUS,LINE_WIDTH,PLAYER_TURN_SPEED,PLAYER_SPEED,PLAYER_SHOOT_SPEED,PLAYER_SHOOT_COOLDOWN_SECONDS
from shot import Shot

class Player(CircleShape):
	def __init__(self, x, y):
		super().__init__(x, y, PLAYER_RADIUS)
		self.rotation = 0
		self.shot_cooldown = 0

		# in the Player class
	def triangle(self):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
		a = self.position + forward * self.radius
		b = self.position - forward * self.radius - right
		c = self.position - forward * self.radius + right
		return [a, b, c]

	def draw(self, screen):
		# overridden
		pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

	def rotate(self, dt):
		self.rotation += PLAYER_TURN_SPEED * dt

	def shoot(self):
		bullet = Shot(self.position.x, self.position.y)

		# start with a unit vector pointing up.
		unit_vector = pygame.Vector2(0, 1)

		# rotate the vector by self.rotation.
		rotated_vector = unit_vector.rotate(self.rotation)

		# take account of PLAYER_SHOOT_SPEED
		rotated_with_speed_vector = rotated_vector * PLAYER_SHOOT_SPEED

		# update the position of the bullet.
		bullet.velocity = rotated_with_speed_vector

	def move(self, dt):
		# start with a unit vector pointing up.
		unit_vector = pygame.Vector2(0, 1)

		# rotate the vector by self.rotation.
		rotated_vector = unit_vector.rotate(self.rotation)

		# take account of PLAYER_SPEED
		rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt

		# update our position.
		self.position += rotated_with_speed_vector

	def update(self, dt):
		# overridden
		if self.shot_cooldown > 0:
			self.shot_cooldown -= dt
		keys = pygame.key.get_pressed()
		if keys[pygame.K_a]:
			# left
			self.rotate(-dt)
		if keys[pygame.K_d]:
			# right
			self.rotate(dt)
		if keys[pygame.K_s]:
			# down
			self.move(-dt)
		if keys[pygame.K_w]:
			# up
			self.move(dt)
		if keys[pygame.K_SPACE]:
			# shoot
			if self.shot_cooldown > 0:
				# don't allow shooting
				print("cooldown period")
			else:
				self.shot_cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS
				self.shoot()

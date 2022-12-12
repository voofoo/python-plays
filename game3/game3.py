import pygame
pygame.init()

clock = pygame.time.Clock()
FPS = 27 

# Create Game Window
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 540

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set window caption
pygame.display.set_caption("Game3")

# Define Variables

scroll = 0

# Ground 
ground = pygame.image.load("ground.png").convert_alpha()
ground_width = ground.get_width()
ground_height = ground.get_height()

# Hero 
walkRight = [pygame.image.load("assets/100x100/z1r.png"), pygame.image.load("assets/100x100/z2r.png"), pygame.image.load("assets/100x100/z3r.png"), pygame.image.load("assets/100x100/z4r.png"), pygame.image.load("assets/100x100/z5r.png"), pygame.image.load("assets/100x100/z6r.png"), pygame.image.load("assets/100x100/z7r.png"), pygame.image.load("assets/100x100/z8r.png"), pygame.image.load("assets/100x100/z9r.png")]
walkLeft = [pygame.image.load("assets/100x100/z1l.png"), pygame.image.load("assets/100x100/z2l.png"), pygame.image.load("assets/100x100/z3l.png"), pygame.image.load("assets/100x100/z4l.png"), pygame.image.load("assets/100x100/z5l.png"), pygame.image.load("assets/100x100/z6l.png"), pygame.image.load("assets/100x100/z7l.png"), pygame.image.load("assets/100x100/z8l.png"), pygame.image.load("assets/100x100/z9l.png")]
hero = pygame.image.load("assets/100x100/standing.png")

x = 50
y = 358
width = 84
height = 100
velocity = 10
left = False
right = False
stepsCount = 0

Jump = False
jumpCount = 10

# Create list of parallax images for background
bg_prlx = []
for i in range(1, 5):
	bg_image = pygame.image.load(f"prlx-{i}.png").convert_alpha()
	bg_prlx.append(bg_image)
bg_width = bg_prlx[0].get_width()

# Create the parallax background by going trhough the list
def draw_prlx_bkgrnd():
	for x in range(5):
		prlx_speed = 1
		for i in bg_prlx:
			window.blit(i, ((x * bg_width) - scroll * prlx_speed, 0))
			prlx_speed += 0.1

# Make ground repeat itself while scrolling
def draw_ground():
	for x in range(15):
		window.blit(ground, ((x * ground_width) - scroll * 2.2, SCREEN_HEIGHT - ground_height))

def drawGameWindow():
	global stepsCount 
	if stepsCount +1 >= 27:
		stepsCount = 0
	if left:
		window.blit(walkLeft[stepsCount//3], (x,y))
		stepsCount += 1
	elif right:
		window.blit(walkRight[stepsCount//3], (x,y))
		stepsCount += 1
	else:
		window.blit(hero, (x,y))

	pygame.display.update()

# Le Game Loope
is_game_running = True

while is_game_running:
	clock.tick(FPS)

	# Draw the parallax
	draw_prlx_bkgrnd()
	draw_ground()
	drawGameWindow()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			is_game_running = False
	
	# Check for keys pressed
	keypress = pygame.key.get_pressed()

	if keypress[pygame.K_LEFT] and scroll > 0:
		scroll -= 5		

	if keypress[pygame.K_RIGHT] and scroll < 3000:
		scroll += 5
		
	if keypress[pygame.K_LEFT] and x > velocity:
		x -= velocity
		left = True
		right = False
	elif keypress[pygame.K_RIGHT] and x < 800 - width - velocity:
		x += velocity
		left = False
		right = True
	else:
		right = False
		left = False
		stepsCount = 0

	if not(Jump):
		if keypress[pygame.K_SPACE]:
			Jump = True
			right = False
			left = False
			stepsCount = 0
	else:
		if jumpCount >= -10:
			neg = 1
			if jumpCount < 0:
				neg = -1
			y -= (jumpCount ** 2) * 0.3 * neg
			jumpCount -= 1 
		else:
			Jump = False
			jumpCount = 10	

pygame.quit()

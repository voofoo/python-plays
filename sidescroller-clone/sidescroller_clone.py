# Sidescroller clone, completed while following the tutorials  
# at https://www.youtube.com/watch?v=AY9MnQ4x3zk

# TODO: make baddies behave properly
# TODO: add a way for hero to attack
# TODO: add sfx
# TODO: add music


import pygame
from sys import exit
from random import randint

def display_score():
	current_time = int(pygame.time.get_ticks() / 1000) - start_game_time # Get time in  
	scoreboard_surface = score_sign.render(f'Points: {current_time}', False, 'Orange')
	scoreboard_rectangle = scoreboard_surface.get_rect(center = (500, 50))
	window.blit(scoreboard_surface, scoreboard_rectangle)
	return current_time

def baddie_moves(baddie_list):
	if baddie_list:
		for baddies_rectangle in baddie_list:
			baddies_rectangle.x -= 5

			if baddies_rectangle.bottom == 300:
				window.blit(baddies_surface, baddies_rectangle)
			else:
				window.blit(baddies2_surface, baddies_rectangle)

		baddie_list = [baddie for baddie in baddie_list if baddie.x > -100]

		return baddie_list
	else:
		return [] # Returns an empty list of baddies if game is running first time

def collision_logic(hero, baddies):
	if baddies:
		for baddies_rectangle in baddies:
			if hero.colliderect(baddies_rectangle):
				return False
	return True

pygame.init()
window = pygame.display.set_mode((1000,500)) # Create game window
pygame.display.set_caption("Project 2 - The Sidescroller Chronicles") # Window title
label_sign = pygame.font.Font('PolandCannedIntoFuture-OxE3.ttf', 50) # Set font for sign
score_sign = pygame.font.Font('DkHandRegular-orna.ttf', 50) # Set font for scoreboard
frameguard = pygame.time.Clock() # Guard framerate
game_running = False
start_game_time = 0
score = 0

# UI Area & Surfaces

game_surface = pygame.image.load('bckgr.png').convert()
ground_surface = pygame.image.load('bckgr2.png').convert()

sign_surface = label_sign.render('The Game', False, 'Orange')
sign_rectangle = sign_surface.get_rect(center = (120,50))

baddies_surface = pygame.image.load('baddie1.png').convert_alpha() # USE .convert_alpha() to balance the alpha channel on .png
baddies2_surface = pygame.image.load("baddie2/2.png").convert_alpha()

baddies_rect_list = []

hero_surface = pygame.image.load('hero1.png').convert_alpha() 
hero_rectangle = hero_surface.get_rect(midbottom = (50,350)) # hero_rect
hero_gravity = 0

# Start Screen
start_screen = pygame.image.load("start1.png").convert_alpha()
start_screen_rect = start_screen.get_rect(center = (500,250))

start_prompt_top = label_sign.render("The game", False, "#FFFFFF")
start_prompt_top_rect = start_prompt_top.get_rect(center = (500, 200))
start_prompt_bottom = label_sign.render("Press space to start", False, "#ffffff")
start_prompt_bottom_rect = start_prompt_bottom.get_rect(center = (500, 325))

# Timer
enemy_timer = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_timer, 1600)

# Le Game Loope
while True: 
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		if game_running:	
			if event.type == pygame.MOUSEBUTTONDOWN:
				if hero_rectangle.collidepoint(event.pos) and hero_rectangle.bottom >= 350:
					hero_gravity = -25
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE and hero_rectangle.bottom >= 350:
					hero_gravity = -25
		else:
			if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
				game_running = True
				hero_rectangle.right = 21
				start_game_time = int(pygame.time.get_ticks() / 1000)

		if event.type == enemy_timer and game_running:
			if randint(0,2):
				baddies_rect_list.append(baddies_surface.get_rect(midbottom =(randint(1010,1210),350)))
			else:
				baddies_rect_list.append(baddies2_surface.get_rect(midbottom =(randint(1010,1210),210)))

	if game_running:
		window.blit(ground_surface,(0,350)) # Ground level 
		window.blit(game_surface,(0,0))
		window.blit(sign_surface, sign_rectangle) # Game title & score
		score = display_score()
		
		# Hero Section
		hero_gravity += 1
		window.blit(hero_surface, hero_rectangle)
		hero_rectangle.y += hero_gravity # Hero gravity
		if hero_rectangle.bottom >= 350:
			hero_rectangle.bottom = 350
		hero_rectangle.left += 2 # Hero speed

		# Obstacles
		baddies_rect_list = baddie_moves(baddies_rect_list)

		# Collisions
		game_running = collision_logic(hero_rectangle,baddies_rect_list)

		# Game end
	else:
		window.fill("orange")
		window.blit(start_screen, start_screen_rect)
		baddies_rect_list.clear()
		hero_rectangle.midbottom = (21, 350)
		hero_gravity = 0
		
		score_message = label_sign.render(f'You scored: {score} points', False, "#FFFFFF")
		score_message_rect = score_message.get_rect(center = (500,325))
		window.blit(start_prompt_top, start_prompt_top_rect)
		
		if score == 0:
			window.blit(start_prompt_bottom, start_prompt_bottom_rect)
		else:
			window.blit(score_message, score_message_rect)

	pygame.display.update() # Updates game window, redraws everything
	frameguard.tick(60) # Targeting rates per second during game loop

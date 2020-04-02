""" This is a game where a car is trying to surpass obsatcles. """
import pygame
import sys
import random
import math
from road import Car, Obastcles
from tkinter import messagebox


# Starting the program
pygame.init()
clock = pygame.time.Clock()

# Basic colors
white = (255, 255, 255)
black = (0, 0, 0)
dark_blue = (141, 226, 218)
red = (255, 0, 0)
maroon = (128, 0, 0)
pink = (244, 52, 131)
lightblue = (27, 238, 255)
grey = (129, 137, 129)
brown = (139,69,19)

# Making the screen
screen_height = 600
screen_width = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Car Game")



# Making the car
player = Car(40, 60, 10)
player.locations(screen_width / 2 - 20,  screen_height - 100) 

# Making the obstacles

# Obstacles objects
Obs1 = Obastcles()
Obs2 = Obastcles()
Obs3 = Obastcles()
Obs4 = Obastcles()
Obs5 = Obastcles()
Obs6 = Obastcles()
Obs7 = Obastcles()

# Spqning Obstacles
Obs1.locations()
Obs2.locations()
Obs3.locations()
Obs4.locations()
Obs5.locations()
Obs6.locations()
Obs7.locations()


# While loop Flag variable
run = True

# Game main loop
while run:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()
    screen.fill(black)

    # Controlling the player
    player.mover()
    player.move_checker()
    player.draw(screen)

    # Controlling the Obstacles
    
    # Moving the obstacles down th eroad
    Obs1.mover()
    Obs2.mover()
    Obs3.mover()
    Obs4.mover()
    Obs5.mover()
    Obs6.mover()
    Obs7.mover()

    # Drawing the Obsatcles to the screen
    Obs1.draw(screen)
    Obs2.draw(screen)
    Obs3.draw(screen)
    Obs4.draw(screen)
    Obs5.draw(screen)
    Obs6.draw(screen)
    Obs7.draw(screen)

    # After the first wave is off the screen this function will revive them.
    Obs1.another_wave()
    Obs2.another_wave()
    Obs3.another_wave()
    Obs4.another_wave()
    Obs5.another_wave()  
    Obs6.another_wave()
    Obs7.another_wave() 

    # Detecting collisions (By calculating the distance from the car to the obstacle)
    player.distance(Obs1, screen)
    player.distance(Obs2, screen)
    player.distance(Obs3, screen)
    player.distance(Obs4, screen)
    player.distance(Obs5, screen)
    player.distance(Obs6, screen)
    player.distance(Obs7, screen)

    # Presenting the score (wave number)
    player.display_score(screen, Obs1)
    
    # Program Clock (60FPS)
    clock.tick(60)
    pygame.display.update()

pygame.quit()
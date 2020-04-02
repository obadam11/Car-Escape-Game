""" The classes needed to the car.py file """
import pygame
import random
import math
from tkinter import messagebox
import sys

# Global scope variables (for both classes)

# Color tuples
white = (255, 255, 255)
black = (0, 0, 0)
dark_blue = (141, 226, 218)
red = (255, 0, 0)
maroon = (128, 0, 0)
pink = (244, 52, 131)
lightblue = (27, 238, 255)
grey = (129, 137, 129)
brown = (160,82,45)

# Screen dimensions
screen_height = 600
screen_width = 600

class Car:
    """ Making the player class which is a car (This class should interact with the Obastacle class) """
    def __init__(self, width, length, vel):
        self.width = width
        self.length = length
        self.vel = vel

    def locations(self, x, y):
        """ Spawning the car at x, y location """
        self.x = x
        self.y = y
        self.xVelocity = 0

    def draw(self, game_screen, color=lightblue):
        """ Drawing the car on the screen. """
        pygame.draw.rect(game_screen, color, (self.x, self.y, self.width, self.length))
    
    def mover(self):
        """ Making the car listen to keyboard inputs """
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.xVelocity = - self.vel
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.xVelocity = self.vel
        else:
            self.xVelocity = 0

    def move_checker(self):
        """ Changing the X location of the car, and setting boundries to the screen. """
        self.x += self.xVelocity

        # Boundries
        if self.x > screen_width - self.width:
            self.x = screen_width - self.width
        if self.x < 0:
            self.x = 0

    def get_coordinates(self):
        """ (A function for debugging) return an X, Y locations as a list"""
        return [self.x, self.y]

    @classmethod
    def get_high_score(cls):
        """ A class method to open txt file and return the high score """
        try:
            with open("scores.txt") as f_read:
                score = f_read.readlines()
        except FileNotFoundError:
            print("This file is not found!")
        else:
            print(score)
            try:
                high_score = max(score)
            except ValueError:
                high_score = 0
        return high_score


    
    def distance(self, other, game_screen):
        """ Calculating the distance between the car(self) and the Obsatcle (other) to detect collsion and 
            close the window """
        crash = False
        x_diff = (self.x - other.x) **2
        y_diff = (self.y - other.y) **2
        dis = (x_diff + y_diff) **0.5
        if dis < 30:
            crash = True

        # Maniging the scores messages
        new_high = False
        if crash: # If the car crashes
            try:
                highest = Car.get_high_score() # Get the high score from the scores.txt file
            except ValueError:
                highest = 0
            if int(other.num_of_waves) > int(highest): # If you got a new high score
                print("New High score")
                new_high = True
            if new_high: 
                print("Collision occured")
                highest = Car.get_high_score()
                pop_up = f"Current score: {other.num_of_waves}\nOld high score: {highest}\nCongrats New High Score!"
                messagebox.showinfo(title="Scores", message=pop_up)
                try:
                    highest = highest[-3:]
                except TypeError:
                    pass
            if not new_high: # If you didn't get a high score (Note: you can use "else" statment here)
                print("Collision occured")
                pop_up = f"Current score: {other.num_of_waves}\nHigh score: {highest}"
                messagebox.showinfo(title="Scores", message=pop_up)
                highest = highest[-3:]
            # To close the pygame window

            # Writing into the scores.txt file
            try:
                with open("scores.txt", "a") as file_w:
                    file_w.write(f'{other.num_of_waves}\n')
            except FileNotFoundError:
                print("File is not found")


            sys.exit()

            
            
    def display_score(self, game_screen, obj, color=white):
        """ Making the score section on the top left corner of the screen. """
        if obj.y >= screen_height - obj.width + 5:
            obj.num_of_waves += 1
        on_screen = f"Score: {obj.num_of_waves}"
        font = pygame.font.Font(None, 50)
        text = font.render(str(on_screen), 1, color)
        game_screen.blit(text, (10,10))


            
            
# The Obstacles class (Enemies)




class Obastcles:
    """ This class make the enemies  """

    num_of_waves = 0

    def __init__(self):
        self.width = 40
        self.length= 60
        self.vel = 3
        

    def locations(self):
        """ Spawning the Enemies at random locations """
        self.x = random.randint(10, screen_width - 40)
        self.y = 20
        self.yVelocity = 0 
    
    def draw(self, game_screen, color=pink):
        """ Drawing the Obstacles """
        pygame.draw.rect(game_screen, color, (self.x, self.y, self.width, self.length))

    def mover(self):
        """ Change the obsatcle location on the Y axis. """
        self.yVelocity = self.vel
        self.y += self.yVelocity

    def another_wave(self):
        """ Making a new wave after passing the previous one. """
        if self.y >= screen_height - self.width + 5:
            self.x = random.randint(10, screen_width - 40)
            self.y = 20
            self.num_of_waves += 1
            # print(f" wave number : {self.num_of_waves}")

            if self.num_of_waves % 5 == 0:
                self.vel += 1

    def get_coordinates(self):
        """ (A function for debugging) return an X, Y locations as a list"""
        return [self.x, self.y] 

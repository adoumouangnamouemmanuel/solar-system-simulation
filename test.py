# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 08:48:42 2024.

@authors: emmanuel.adoum & Rachel.

@Module: Main module of the program.
"""

# main.py
import pygame
import os
from SolarSystem import SolarSystem
from Planet import Planet
from Star import Star
from Moon import Moon
# from load_data import load_file, lst
import load_data


pygame.init()

WIDTH, HEIGHT = 1600, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solar System Simulation")

# Constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (100, 149, 237)
GREY = (169, 169, 169)
ORANGE = (255, 165, 0)
RED = (188, 39, 50)
DARK_GREY = (80, 78, 81)
R_SCALE = 696340 / 30 # Scaling down the radius

FONT = pygame.font.SysFont("comicsans", 16)


def main():
    """Main-function to run the solar system simulation using Pygame."""
    path = os.getcwd()
    file_name = 'data.csv'
    file_path = os.path.join(path, file_name)
    
    # lst = load_file(file_path)
    lst = load_data.lst
    print(lst)
    solar_system = SolarSystem(WIDTH, HEIGHT)
    
    for planet in lst:
        name = planet['Name']
        mass = float(planet['Mass'])
        dist = float(planet['Distance from sun'])
        radius = float(planet['Radius']) / R_SCALE
        color = planet['color'] 
        moonNum = int(planet['moonNum'])
        x = float(planet['x in AU'] )* Planet.AU
        print(x)
        y = int(planet['y'])
        y_velocity = float(planet['y_vel'])
        plan = Planet(x, y, radius, color, mass, name, dist)
        plan.y_vel = y_velocity
        print(planet)
        solar_system.add_planet(plan)
       

    #  # Create the Sun
    # sun = Planet(0, 0, 30/R_SCALE, YELLOW, 1.98892 * 10 ** 30, iname="Sun")
    # sun.sun = True
    # solar_system.add_planet(sun)
    
    # # Create Mercury
    # mercury = Planet(0.387 * Planet.AU, 0, 8/R_SCALE,
    #                  DARK_GREY, 3.30e23, iname="Mercury")
    # mercury.y_vel = -47.4 * 1000  # km/s converted to m/s
    # solar_system.add_planet(mercury)

    # # Create Venus
    # venus = Planet(0.723 * Planet.AU, 0, 14/R_SCALE, ORANGE, 4.8685e24, iname="Venus")
    # venus.y_vel = -35.02 * 1000
    # solar_system.add_planet(venus)

    # # Create Earth
    # earth = Planet(-Planet.AU, 0, 16/R_SCALE, BLUE, 5.9742e24, iname="Earth")
    # earth.y_vel = 29.783 * 1000
    # solar_system.add_planet(earth)

    # # Create Mars
    # mars = Planet(-1.524 * Planet.AU, 0, 12/R_SCALE, RED, 6.39e23, iname="Mars")
    # mars.y_vel = 24.077 * 1000
    # solar_system.add_planet(mars)

    # # Create Jupiter
    # jupiter = Planet(-5.203 * Planet.AU, 0, 24/R_SCALE, ORANGE, 1.898 * 10 ** 27, iname="Jupiter")
    # jupiter.y_vel = 13.07 * 1000
    # solar_system.add_planet(jupiter)
    
    # # Jupiter's Moons (79 total, only showing 4 main ones)
    # for i in range(4):
    #     jupiter_moon = Moon(0, 0, 3, GREY, 1.08 * 10 ** 23, (70 + i * 10) / 3, 0.04 + 0.02 * i, jupiter)
    #     jupiter.add_moon(jupiter_moon)
    
    # # Create Saturn
    # saturn = Planet(-9.539 * Planet.AU, 0, 28/R_SCALE, DARK_GREY, 5.683 * 10 ** 26, iname="Saturn")
    # saturn.y_vel = 9.68 * 1000
    # solar_system.add_planet(saturn)
    
    # # Saturn's Moons (83 total, Titan is the largest)
    # for i in range(6):
    #     saturn_moon = Moon(0, 0, 3, GREY, 1.08 * 10 ** 23, (80 + i * 10) / 3, 0.03 + 0.02 * i, saturn)
    #     saturn.add_moon(saturn_moon)
    
    # # Create Uranus
    # uranus = Planet(-19.18 * Planet.AU, 0, 24/R_SCALE, GREY, 8.681 * 10 ** 25, iname="Uranus")
    # uranus.y_vel = 6.80 * 1000
    # solar_system.add_planet(uranus)
    
    # # Uranus's Moons (27 total, 5 major ones)
    # for i in range(5):
    #     uranus_moon = Moon(0, 0, 3, WHITE, 1.08 * 10 ** 23, (60 + i * 10) / 3, 0.05 + 0.02 * i, uranus)
    #     uranus.add_moon(uranus_moon)
    
    # # Create Neptune
    # neptune = Planet(-30.07 * Planet.AU, 0, 22/R_SCALE, BLUE, 1.024 * 10 ** 26, iname="Neptune")
    # neptune.y_vel = 5.43 * 1000
    # solar_system.add_planet(neptune)

    # solar_system.add_planet(venus)


# # Add moons
#     moon = Moon(0, 0, 3, GREY, 7.35 * 10**22, 40/3, 0.06, earth)
#     phobos = Moon(0, 0, 2, GREY, 1.08 * 10**16, 10/3, 0.07, mars)
#     deimos = Moon(0, 0, 2, WHITE, 1.80 * 10**15, 15/3, 0.05, mars)

#     earth.add_moon(moon)
#     mars.add_moon(phobos)
#     mars.add_moon(deimos)

    for _ in range(500):  # Add 1000 stars for the background
        star = Star(WIDTH, HEIGHT)
        solar_system.add_star(star)

    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(60)
        WIN.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        solar_system.update()  # Update all celestial bodies
        solar_system.draw(WIN)  # Draw all celestial bodies

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()

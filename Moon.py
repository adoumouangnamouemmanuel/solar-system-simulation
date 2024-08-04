# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 20:40:36 2024.

@author: emmanuel.adoum & Rachel

@Module: Moon module
"""

# moon.py
import pygame
import math
from Planet import Planet
pygame.init()
FONT = pygame.font.SysFont("comicsans", 16)
WHITE = (255, 255, 255)


class Moon:
    """Represents a Moon that orbits around a planet."""

    SCALE = Planet.SCALE #30 / (149.6e6 * 1000)  # Use the same scale as the planet

    def __init__(self, x, y, radius, color, mass, orbit_radius,
                 orbit_speed, planet):
        """
        Initialize a Moon.

        --------------

        Args:
        ----
            x (float): Initial x-coordinate (relative to the planet).
            y (float): Initial y-coordinate (relative to the planet).
            radius (int): Radius for drawing.
            color (tuple): RGB color.
            mass (float): Mass of the moon.
            orbit_radius (float): Radius of the moon's orbit around the planet.
            orbit_speed (float): Angular speed of the moon's orbit.
            planet (Planet): The planet around which this moon orbits.
        """
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass
        self.orbit_radius = orbit_radius
        self.orbit_speed = orbit_speed
        self.planet = planet
        self.angle = 0

    def draw(self, win):
        """
        Draw the moon on the Pygame window.

        Args:
        ----
            win (pygame.Surface): The surface to draw on.
        """
        x = self.planet.x * Moon.SCALE + win.get_width() / 2
        y = self.planet.y * Moon.SCALE + win.get_height() / 2
        moon_x = x + self.orbit_radius * math.cos(self.angle)
        moon_y = y + self.orbit_radius * math.sin(self.angle)

        pygame.draw.circle(win, self.color,
                           (int(moon_x), int(moon_y)), self.radius)

    def update_position(self):
        """Update the position of the moon based on its orbit.

        around the planet.
        """
        self.angle += self.orbit_speed

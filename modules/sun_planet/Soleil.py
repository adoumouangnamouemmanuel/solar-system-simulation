# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 08:09:53 2024.

@authors: emmanuel.adoum & Rachel

@Module: Defines the Sun Planet
"""
# sun.py
import pygame

from modules.sun_planet.Planet import Planet


class Sun(Planet):
    """Represents the Sun with specific attributes for simulation in Pygame."""

    def __init__(self, x, y, radius=30, color=(255, 255, 0), mass=1.98892e30):
        """
        Initialize the Sun.

        Args:
        ----
            x (float): The x-coordinate of the Sun.
            y (float): The y-coordinate of the Sun.
            radius (int): The radius of the Sun.
            color (tuple): RGB color of the Sun.
            mass (float): Mass of the Sun.
        """
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass
        self.sun = True  # Mark this as the sun for specific behaviors

    def draw(self, win):
        """
        Draw the Sun on the Pygame window.

        Args:
        ----
            win (pygame.Surface): The surface to draw on.
        """
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

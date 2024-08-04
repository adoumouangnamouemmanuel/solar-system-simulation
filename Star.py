# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 08:42:54 2024.

@author: emmanuel.adoum & Rachel

@Module: Defines the stars class
"""

import pygame
import random
import math


class Star:
    """Represents a Star with random movement in the Pygame simulation."""

    def __init__(self, width, height):
        """
        Initialize a Star.

        Args:
        ----
            width (int): Width of the simulation window.
            height (int): Height of the simulation window.
        """
        self.x = random.uniform(-width / 2, width / 2)
        self.y = random.uniform(-height / 2, height / 2)
        self.size = random.uniform(0.00001, 0.0003)
        self.color = (255, 255, 255)  # White color
        self.dx = random.uniform(-1, 1) * 0.5
        self.dy = random.uniform(-1, 1) * 0.5
        self.radius = 2  # Radius for the star's central part

    def draw_star(self, win, center, radius, color):
        """
        Draw a star shape on the Pygame surface.

        Args:
        ----
            win (pygame.Surface): The surface to draw on.
            center (tuple): The (x, y) coordinates of the center of the star.
            radius (float): The radius of the star.
            color (tuple): The color of the star.
        """
        num_points = 5
        points = []
        for i in range(num_points * 2):
            angle = i * math.pi / num_points
            if i % 2 == 0:
                length = radius
            else:
                length = radius / 2
            x = center[0] + length * math.cos(angle)
            y = center[1] + length * math.sin(angle)
            points.append((x, y))

        pygame.draw.polygon(win, color, points)

    def draw(self, win):
        """
        Draw the star on the Pygame window.

        Args:
        ----
            win (pygame.Surface): The surface to draw on.
        """
        x = self.x + win.get_width() / 2
        y = self.y + win.get_height() / 2
        self.draw_star(win, (x, y), self.radius, self.color)

    def move(self, width, height):
        """
        Move the star randomly within the window boundaries.

        Args:
        ----
            width (int): Width of the window.
            height (int): Height of the window.
        """
        self.x += self.dx
        self.y += self.dy

        # Wrap around the screen
        if self.x > width / 2:
            self.x = -width / 2
        elif self.x < -width / 2:
            self.x = width / 2

        if self.y > height / 2:
            self.y = -height / 2
        elif self.y < -height / 2:
            self.y = height / 2

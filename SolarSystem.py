# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 08:24:31 2024.

@authors: emmanuel.adoum & Rachel

@Module: Defines the SolarSystem class
"""
# solar_system.py


class SolarSystem:
    """
    Represents the Solar System with the Sun, planets.

    and stars for simulation
    """

    def __init__(self, width, height):
        """
        Initialize the Solar System.

        Args:
        ----
            width (int): Width of the simulation window.
            height (int): Height of the simulation window.
        """
        self.width = width
        self.height = height
        self.sun = None
        self.planets = []
        self.stars = []
        self.bg_color = (0, 0, 0)  # Black background color

    def add_sun(self, sun):
        """
        Add the Sun to the solar system.

        Args:
        ----
            sun (Sun): The Sun object to add.
        """
        self.sun = sun

    def add_planet(self, planet):
        """
        Add a planet to the solar system.

        Args:
        ----
            planet (Planet): The planet object to add.
        """
        self.planets.append(planet)

    def add_star(self, star):
        """
        Add a star to the solar system.

        Args:
        ----
            star (Star): The star object to add.
        """
        self.stars.append(star)

    def draw(self, win):
        """
        Draw the entire solar system on the Pygame window.

        Args:
        ----
            win (pygame.Surface): The surface to draw on.
        """
        win.fill(self.bg_color)  # Fill the background

        for star in self.stars:
            star.draw(win)

        if self.sun:
            self.sun.draw(win)

        for planet in self.planets:
            planet.draw(win)

    def move_stars(self):
        """Move all stars in the solar system."""
        for star in self.stars:
            star.move(self.width, self.height)

    def update(self):
        """Update the positions of all celestial bodies in the solar system."""
        self.move_stars()
        for planet in self.planets:
            planet.update_position(self.planets)

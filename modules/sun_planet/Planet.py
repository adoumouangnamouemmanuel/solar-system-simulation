# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 02:05:45 2024.

@authors: emmanuel.adoum & Rachel

@Module: Defines the Planet Class
"""

import pygame
import math
import csv
pygame.init()
FONT = pygame.font.SysFont("comicsans", 16)
WHITE = (255, 255, 255)


class Planet:
    """Represents a Planet with physics simulation and drawing in Pygame."""

    AU = 149.6e6 * 1000  # Astronomical Unit in meters
    G = 6.67430e-11  # Gravitational constant (updated value)
    SCALE = 25 / AU  # Scale for drawing distances in Pygame
    TIMESTEP = 3600 * 24  # 1 day in seconds

    def __init__(self, x, y, radius, color, mass,
                 iname="Earth", idist=1.49, inm=1):
        """
        Initialize a new Planet.

        Args:
        ----
            x (float): Initial x-coordinate.
            y (float): Initial y-coordinate.
            radius (int): Radius for drawing.
            color (tuple): RGB color.
            mass (float): Mass of the planet.
            iname (str): Name of the Planet
            idist (float): Distance from the Sun
            inm (int): Number of moons
        """
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass
        self.name = iname
        self.numMoons = inm
        self.distance = idist

        self.orbit = []
        self.moons = []
        self.sun = False  # Mark if this is the Sun
        self.distance_to_sun = 0

        self.x_vel = 0
        self.y_vel = 0

    def __str__(self):
        """String-Representation of a Planet."""
        return self.name

    def __repr__(self):
        """String-Representation of a Planet."""
        return self.name

    # Getters
    @property
    def getName(self):
        """Get the name of the Planet."""
        return self.name

    @property
    def getNumMoons(self):
        """Get the number of moons."""
        return self.numMoons

    @property
    def getMass(self):
        """Get the Planet's Mass."""
        return self.mass

    @property
    def getRadius(self):
        """Get the radius of the Planet."""
        return self.radius

    @property
    def getDistance(self):
        """Get Planet's distance from the Sun."""
        return self.distance

    @property
    def getMoonList(self):
        """Get the list of moons."""
        return self.moons

    # Setters
    @getName.setter
    def setName(self, iname):
        """Set the Planet's name."""
        self.name = iname

    @getNumMoons.setter
    def setNumMoons(self, inm):
        """Set the Planet's number of moons."""
        self.numMoons = inm

    @getMass.setter
    def setMass(self, im):
        """Set the Planet's Mass."""
        self.mass = im

    @getRadius.setter
    def setRadius(self, irad):
        """Set the Planet's radius."""
        self.radius = irad

    @getDistance.setter
    def setDistance(self, idist):
        """Set the Planet's distance from sun."""
        self.distance = idist

    # Calculations
    def getVolume(self):
        """Calculate the volume of the planet assuming it is a sphere."""
        return (4 / 3) * math.pi * self.radius ** 3

    def getDensity(self):
        """Calculate the density of the planet."""
        return self.mass / self.getVolume()

    def getSurfaceArea(self):
        """Calculate the surface area of the planet."""
        return 4 * math.pi * self.radius ** 2

    def getCircumference(self):
        """Calculate the circumference of the planet."""
        return 2 * math.pi * self.radius

    def getGravity(self):
        """Calculate the surface gravity of the planet."""
        return self.G * self.mass / self.radius ** 2

    def getOrbitalPeriod(self):
        """Calculate the orbital period of the planet.

        Uses Kepler's third law of planetary motion:
        T^2 / r^3 = 4 * pi^2 / (G * M_sun)
        """
        # mass of the Sun
        return 2 * math.pi * math.sqrt(self.distance ** 3
                                       / (self.G * 1.989e30))

    def getEscapeVelocity(self):
        """Calculate the escape velocity of the planet."""
        return math.sqrt(2 * self.G * self.mass / self.radius)

    def getOrbitalVelocity(self):
        """Calculate the orbital velocity of the planet."""
        return math.sqrt(self.G * self.mass / self.distance)

    def draw(self, win):
        """
        Draw the planet and its orbit on the Pygame window.

        Args:
        ----
            win (pygame.Surface): The surface to draw on.
        """
        x = self.x * self.SCALE + win.get_width() / 2
        y = self.y * self.SCALE + win.get_height() / 2

        if len(self.orbit) > 2:
            updated_points = [(x * self.SCALE + win.get_width() / 2,
                               y * self.SCALE + win.get_height() / 2)
                              for (x, y) in self.orbit]
            pygame.draw.lines(win, self.color, False, updated_points, 2)

        pygame.draw.circle(win, self.color, (int(x), int(y)), self.radius)

        for moon in self.moons:
            moon.draw(win)
        if not self.sun:
            distance_text = FONT.render(f"{self.name[0]}", 1, WHITE)
            win.blit(distance_text, (x - distance_text.get_width() / 2,
                                     y - distance_text.get_height() / 2))

    def attraction(self, other):
        """
        Calculate the gravitational attraction between this planet and another.

        Args:
        ----
            other (Planet): The other celestial body.

        Returns
        -------
            tuple: (force_x, force_y) force exerted on this body.
        """
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x**2 + distance_y**2)

        if other.sun:
            self.distance_to_sun = distance

        force = self.G * self.mass * other.mass / distance**2
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force

        return force_x, force_y

    def update_position(self, planets):
        """
        Update the position of the planet based on gravitational forces.

        Args:
        ----
            planets (list): List of all celestial bodies.
        """
        total_fx = total_fy = 0
        for planet in planets:
            if self == planet:
                continue

            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy

        self.x_vel += total_fx / self.mass * self.TIMESTEP
        self.y_vel += total_fy / self.mass * self.TIMESTEP

        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP
        self.orbit.append((self.x, self.y))

        for moon in self.moons:
            moon.update_position()

    def add_moon(self, moon):
        """
        Add a moon to the planet.

        Args:
        ----
            moon (Moon): The moon to be added.
        """
        self.moons.append(moon)

    def export_to_csv(self, filename='planet_data.csv'):
        """
        Export planet attributes and calculated values to a CSV file.

        Args:
        ----
            filename (str): The name of the CSV file.
        """
        try:
            with open(filename, mode='w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow([
                    'Name', 'X', 'Y', 'Radius', 'Color', 'Mass', 'Distance',
                    'Number of Moons', 'Volume', 'Density', 'Surface Area',
                    'Circumference', 'Gravity',
                    'Orbital Period', 'Escape Velocity', 'Orbital Velocity'
                ])
                writer.writerow([
                    self.name, self.x, self.y, self.radius, self.color,
                    self.mass, self.distance, self.numMoons,
                    self.getVolume(), self.getDensity(),
                    self.getSurfaceArea(), self.getCircumference(),
                    self.getGravity(), self.getOrbitalPeriod(),
                    self.getEscapeVelocity(), self.getOrbitalVelocity()
                ])
        except IOError as e:
            print(f"Failed to write to {filename}: {e}")

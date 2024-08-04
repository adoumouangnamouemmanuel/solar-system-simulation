# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 08:48:42 2024.

@authors: emmanuel.adoum & Rachel.

@Module: Main module of the program.
"""

import pygame

import load_data
from decorators import log_function_call, measure_time
from logger import logger
from Moon import Moon
from Planet import Planet
from SolarSystem import SolarSystem
from Star import Star

pygame.init()

WIDTH, HEIGHT = 1600, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solar System Simulation")

# Constants
GREY = (169, 169, 169)
BLACK = (0, 0, 0)

# Note: Planet radius scale for visualization purposes
R_SCALE = 696340 / 2000  # Scaling down the radius for visualization
SUN_SCALE = 696340 / 50  # Smaller scale for the Sun to fit the window better
Planet.SCALE = 250 / Planet.AU
Moon.SCALE = Planet.SCALE

FONT = pygame.font.SysFont("comicsans", 16)


@log_function_call(logger)
def create_moons(parent_planet, moon_count):
    """Create moons for a given planet."""
    for i in range(moon_count):
        # Randomize some properties for variety
        moon_radius = 5
        moon_distance = (40 + i * 10) / 3
        moon_angle = 0.05 + 0.01 * i
        moon_mass = 7.35 * 10**22  # Example mass

        # Create moon object
        moon = Moon(0, 0, moon_radius, GREY, moon_mass, moon_distance,
                    moon_angle, parent_planet)
        parent_planet.add_moon(moon)


@log_function_call(logger)
@measure_time(logger)
def main():
    """Themain function to run the solar system simulation using Pygame."""
    try:
        # Load planets data
        lst = load_data.lst

        # Check if the list is empty
        if not lst:
            raise ValueError("Error: Planet list is empty.\
                             Data could not be loaded from CSV.")

        # Create solar system
        solar_system = SolarSystem(WIDTH, HEIGHT)

        for planet in lst:
            try:
                # Extract data from CSV
                name = planet['Name']
                mass = float(planet['Mass'])
                color_string = planet['color']
                # Convert color string to tuple
                color = tuple(map(int, color_string.strip('()').split(',')))

                # moon_num = int(planet['moonNum'])
                x = float(planet['x in AU']) * Planet.AU
                y = int(planet['y'])
                # Convert km/s to m/s
                y_velocity = float(planet['y_vel']) * 1000

                # Adjust radius scaling for Sun
                if name == "Sun":
                    # Use SUN_SCALE for the Sun
                    radius = float(planet['Radius']) / SUN_SCALE
                else:
                    # Use R_SCALE for other planets
                    radius = float(planet['Radius']) / R_SCALE

                # Log planet creation
                logger.info(f"Creating {name} at position ({x}, {y})\
                            with radius {radius} and velocity {y_velocity}")

                # Create planet object
                planet_obj = Planet(x, y, radius, color, mass, name)
                planet_obj.y_vel = y_velocity

                # Add planet to solar system
                solar_system.add_planet(planet_obj)

                # Create moons dynamically based on moonNum
                # create_moons(planet_obj, moon_num)

            except KeyError as e:
                logger.error(f"Error processing planet data:\
                             Missing key {e} in CSV for planet {planet}.")
            except ValueError as e:
                logger.error(f"Error processing planet data:\
                             Value error {e} for planet {planet}.")
            except Exception as e:
                logger.error(f"Unexpected error processing planet data:\
                             {e} for planet {planet}.")

            # Break loop for Mars (for testing or specific reasons)
            if name == 'Mars':
                break

        # Add 500 stars for the background
        for _ in range(500):
            star = Star(WIDTH, HEIGHT)
            solar_system.add_star(star)

        clock = pygame.time.Clock()
        run = True

        while run:
            clock.tick(60)
            WIN.fill(BLACK)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            # Update and draw solar system
            solar_system.update()
            solar_system.draw(WIN)

            pygame.display.update()

        pygame.quit()
        logger.info("Simulation ended")

    except ValueError as e:
        logger.error(e)
        print(e)  # Print to console for immediate feedback
    except Exception as e:
        logger.error(f"Unexpected error occurred in the main function: {e}")
    finally:
        # Remove handlers at the end
        remove_handlers(logger)


def remove_handlers(logger):
    """Remove handlers to prevent logging duplication in future runs."""
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)
        handler.close()


if __name__ == "__main__":
    main()

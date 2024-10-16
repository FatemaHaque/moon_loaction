import pygame
import random
from circle import get_pixels
from operator import itemgetter


class Moon:
    def __init__(self, orbit_radius):
        self.radius = 10
        # self.visible = False
        self.orbit_radius = orbit_radius
        self.orbit = get_pixels(200, 200, self.orbit_radius)
        print(self.orbit)
        self.__sort_axis_pixels()
        # print(f"orbit: {self.orbit}")
        self.color = (255, 255, 255)
        # self.zone = random.choice([i for i in range(8)])
        self.zone = 0
        # self.x, self.y = random.choice(self.orbit[self.zone])
        self.x, self.y = self.middle_zone()
        self.rotation = False

    def middle_zone(self):
        """
        This function returns the coordinates of 
        the middle pixel in the current zone of an orbit.
        :return: the coordinates of the pixel in the middle 
        of the current zone of the orbit.
        Specifically, it returns a tuple containing the x and y coordinates of the pixel.
        """
        pos = len(self.orbit[self.zone]) // 2 + len(self.orbit[self.zone]) % 2
        pixel = self.orbit[self.zone][pos]
        return pixel[0], pixel[1]

    def __sort_axis_pixels(self):
        """
        This function sorts the pixels in each orbit based 
        on their position along the x and y axes.
        """
        # `key=itemgetter(n)` is a parameter used in the `sort()` method to specify
        # the sorting criteria. In this case, it is sorting the list of pixels
        # based on the second element of each tuple (i.e., the y-coordinate).
        self.orbit[0].sort(key=itemgetter(1), reverse=True)
        self.orbit[1].sort(key=itemgetter(0), reverse=True)
        self.orbit[2].sort(key=itemgetter(0), reverse=True)
        self.orbit[3].sort(key=itemgetter(1), reverse=False)
        self.orbit[4].sort(key=itemgetter(1), reverse=False)
        self.orbit[5].sort(key=itemgetter(0), reverse=False)
        self.orbit[6].sort(key=itemgetter(0), reverse=False)
        self.orbit[7].sort(key=itemgetter(1), reverse=True)
        # for zone in range(8):
        #     if zone == 0:
        #         self.orbit[zone].sort(key=itemgetter(1), reverse=True)
        #     elif zone == 1:
        #         self.orbit[zone].sort(key=itemgetter(0), reverse=True)
        #     elif zone == 2:
        #         self.orbit[zone].sort(key=itemgetter(0), reverse=True)
        #     elif zone == 3:
        #         self.orbit[zone].sort(key=itemgetter(1), reverse=False)
        #     elif zone == 4:
        #         self.orbit[zone].sort(key=itemgetter(1), reverse=False)
        #     elif zone == 5:
        #         self.orbit[zone].sort(key=itemgetter(0), reverse=False)
        #     elif zone == 6:
        #         self.orbit[zone].sort(key=itemgetter(0), reverse=False)
        #     else:
        #         self.orbit[zone].sort(key=itemgetter(1), reverse=True)

    def draw(self, window):
        """
        This function draws the orbit and moon of a celestial object on a Pygame window.
        
        :param window: The window parameter is the surface object
          representing the game window or screen
        on which the moons and their orbits will be drawn
        """
        # Draw moons orbit
        for i in range(8):
            for pixel in self.orbit[i]:
                window.set_at((pixel[0], pixel[1]), (255, 0, 0))
        # Draw the moon
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)

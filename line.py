import pygame


def find_zone(dx, dy):
    if abs(dx) <= abs(dy):
        if dx >= 0 and dy >= 0:
            return 1
        elif dx <= 0 and dy >= 0:
            return 2
        elif dx >= 0 and dy <= 0:
            return 6
        elif dx <= 0 and dy <= 0:
            return 5
    else:
        if dx >= 0 and dy >= 0:
            return 0
        elif dx <= 0 and dy >= 0:
            return 3
        elif dx >= 0 and dy <= 0:
            return 7
        elif dx <= 0 and dy <= 0:
            return 4


def convert_to_zone0(z, x, y):
    if z == 0:
        return x, y
    elif z == 1:
        return y, x
    elif z == 2:
        return y, -x
    elif z == 3:
        return -x, y
    elif z == 4:
        return -x, -y
    elif z == 5:
        return -y, -x
    elif z == 6:
        return y, -x
    else:
        return x, -y


def convert_original(z, x, y):
    if z == 0:
        return x, y
    elif z == 1:
        return y, x
    elif z == 2:
        return -y, x
    elif z == 3:
        return -x, y
    elif z == 4:
        return -x, -y
    elif z == 5:
        return -y, -x
    elif z == 6:
        return y, -x
    else:
        return x, -y


def midpointline(window, x1, y1, x2, y2, z):
    """
    The function uses the midpoint line algorithm to draw a line between two points on a window.
    
    :param window: The window parameter is the graphics window or canvas on which the line will be drawn
    :param x1: The x-coordinate of the starting point of the line
    :param y1: The y-coordinate of the starting point of the line
    :param x2: The x-coordinate of the end point of the line
    :param y2: The y-coordinate of the second endpoint of the line segment
    :param z: It is not clear from the given code what the parameter z represents. It is possible that
    it is a variable used in the function convert_original, which is not shown in the code snippet.
    Without more context or information, it is difficult to determine the purpose of the z parameter
    """
    dx = x2 - x1
    dy = y2 - y1

    d = (2 * dy) - dx
    e = 2 * dy
    ne = 2 * (dy - dx)

    x = x1
    y = y1

    while x < x2:
        px, py = convert_original(z, x, y)
        draw_pixel(window, px, py)
        if d < 0:
            x += 1
            d += e
        else:
            x += 1
            y += 1
            d += ne


def draw_pixel(window, x, y):

    # pygame.draw.rect(window, (255, 0, 0), (x, y, 15, 15))
    window.set_at((x, y), (255, 0, 0))


def draw_line(window, x1, y1, x2, y2):
    """
    This function draws a line on a window using the midpoint line algorithm after converting the line
    to zone 0.
    
    :param window: It is the window or canvas on which the line will be drawn. 
    It could be a tkinter
    canvas or a pygame window, depending on the context in which this
      function is being used
    :param x1: The x-coordinate of the starting point of the line
    :param y1: Unfortunately, the parameter "y1" is not provided in the
      code snippet you provided. Can
    you please provide more information or context so I can assist you better?
    :param x2: The x-coordinate of the end point of the line
    :param y2: The y-coordinate of the end point of the line to be drawn
    """
    dx = x2 - x1
    dy = y2 - y1

    zone = find_zone(dx, dy)

    px1, py1 = convert_to_zone0(zone, x1, y1)
    px2, py2 = convert_to_zone0(zone, x2, y2)

    midpointline(window, px1, py1, px2, py2, zone)

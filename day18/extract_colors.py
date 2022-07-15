# Extract Colors

import colorgram

def get_colors(image_name):
    rgb_tuples = list()
    colors = colorgram.extract(image_name, 10)
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        rgb_tuples.append((r, g, b))
    return rgb_tuples
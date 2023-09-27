from PIL import Image
from webcolors import (
    CSS3_HEX_TO_NAMES,
    hex_to_rgb,
)
from scipy.spatial import KDTree


def get_hex_value(file):
    image_file = Image.open(file)
    height, width = image_file.size
    center_height = height // 2
    center_width = width // 2
    rgb = image_file.getpixel((center_height, center_width))
    hex_value = ("{:X}{:X}{:X}").format(rgb[0], rgb[1], rgb[2])
    while len(hex_value) < 6:
        hex_value = "0" + hex_value
    return "#" + hex_value


def get_color(rgb_tuple):
    css_db = CSS3_HEX_TO_NAMES
    names = []
    rgb_values = []

    for color_hex, color_name in css_db.items():
        names.append(color_name)
        rgb_values.append(hex_to_rgb(color_hex))

    kdt_db = KDTree(rgb_values)
    distance, index = kdt_db.query(rgb_tuple)
    return names[index]



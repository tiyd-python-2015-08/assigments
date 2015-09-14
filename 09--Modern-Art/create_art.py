# Script to generate random art.
# Adapted by Clinton Dreisbach from code by Chris Stone and Andrew Farmer.

import argparse
import random
import sys
from PIL import Image
from random_art import create_expression, run_expression


def generate_monochrome_image(expression, width=300):
    """Return a grayscale image of the given expression."""
    height = width

    def convert_coords(x, y):
        """Convert absolute coordinates to relative coords
        between (-1, -1) and (1, 1)."""
        width_unit = width / 2
        height_unit = height / 2
        rx = (x - width_unit) / width_unit
        ry = (y - height_unit) / height_unit
        return (rx, ry)

    def scale_intensity(rel_intensity):
        """Convert a relative intensity from [-1, 1] to [0,255]."""
        return int(rel_intensity * 127.5 + 127.5)

    image = Image.new("L", (width, height))

    # Go through each pixel in the image.
    # We will convert each coordinate to a coordinate between
    # (-1, -1) and (1, 1) before passing it to our expression.
    for py in range(height):
        for px in range(width):
            x, y = convert_coords(px, py)
            expr_value = run_expression(expression, x, y)
            intensity = scale_intensity(expr_value)
            image.putpixel((px, py), intensity)

    return image


def generate_rgb_image(red_exp, green_exp, blue_exp, width=300):
    red_image = generate_monochrome_image(red_exp, width)
    green_image = generate_monochrome_image(green_exp, width)
    blue_image = generate_monochrome_image(blue_exp, width)
    return Image.merge("RGB", (red_image, green_image, blue_image))


def make_gray(seed, num_pics=1, width=300):
    """Creates n grayscale image files named gray0.png, gray1.png, ..."""
    random.seed(seed)
    for i in range(num_pics):
        filename = "gray-{}-{}.png".format(seed, i)
        gray_exp = create_expression()
        print("{}: {}".format(filename, gray_exp))
        image = generate_monochrome_image(gray_exp, width)
        image.save(filename, "PNG")


def make_color(seed, num_pics=1, width=300):
    """Creates n color image files named color0.png, color1.png, ..."""
    random.seed(seed)
    for i in range(num_pics):
        filename = "color-{}-{}.png".format(seed, i)
        red_exp = create_expression()
        green_exp = create_expression()
        blue_exp = create_expression()
        print("{}:\n  red: {}\n  green: {}\n  blue: {}".format(filename,
                                                               red_exp,
                                                               green_exp,
                                                               blue_exp))
        image = generate_rgb_image(red_exp, green_exp, blue_exp, width)
        image.save(filename, "PNG")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create random art.')
    parser.add_argument('-S', '--seed', type=int,
                        help="Set the seed for the random number generator.")
    parser.add_argument('-s', '--size', type=int, default=300,
                        help="Number of pixels for each side of the square.")
    parser.add_argument('-n', '--number', type=int, default=1,
                        help="Generate N images.")
    parser.add_argument('--color', action='store_true',
                        help="Generate color images (default).")
    parser.add_argument('--gray', action='store_true',
                        help="Generate grayscale images.")

    args = parser.parse_args()
    if not (args.color or args.gray):
        args.color = True

    if args.seed:
        seed = args.seed
    else:
        seed = random.randint(0, sys.maxsize)

    random.seed(seed)
    print("Seed: {}".format(seed))

    if args.color:
        make_color(seed, args.number, args.size)

    if args.gray:
        make_gray(seed, args.number, args.size)

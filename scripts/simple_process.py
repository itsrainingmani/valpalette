from functools import reduce
import os
import json
from collections import Counter
import pathlib
from PIL import Image


def get_most_common_colors(image_path, num_colors=5):
    with Image.open(image_path) as img:
        img = img.convert("RGB")
        pixels = list(img.getdata())
        color_counts = Counter(pixels)
        most_common_colors = color_counts.most_common(num_colors)
        sum_most_common = reduce(lambda x, y: x + y[1], most_common_colors, 0)
        return [
            {f"#{r:02x}{g:02x}{b:02x}": (c / sum_most_common) * 100}
            for (r, g, b), c in most_common_colors
        ]


def process_directory(directory):
    color_data = {}
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(".png"):
                file_path = os.path.join(root, file)
                colors = get_most_common_colors(file_path)
                color_data[pathlib.Path(file).stem] = colors
    return color_data


def main():
    directories = ["phantom", "vandal"]
    all_colors = {}

    for directory in directories:
        skin_dir = os.path.join("pixelated", directory)
        if os.path.exists(skin_dir):
            all_colors.update(process_directory(skin_dir))
        else:
            print(f"Directory '{directory}' does not exist.")

    # print(all_colors)
    with open("colors.json", "w") as json_file:
        json.dump(all_colors, json_file, indent=4)


if __name__ == "__main__":
    main()

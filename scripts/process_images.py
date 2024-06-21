import json
import os
import pathlib
import cv2
import numpy as np
from sklearn.cluster import KMeans
from collections import Counter


def extract_distinct_colors(image_path, num_colors=10):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image from BGR to RGB color space
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Reshape the image to a 2D array of pixels
    pixels = image.reshape(-1, 3)

    # Perform color quantization using K-means clustering
    kmeans = KMeans(n_clusters=num_colors, random_state=42).fit(pixels)
    labels = kmeans.labels_

    # Count the frequency of each color
    color_counts = Counter(labels)

    # Sort the colors based on their frequency (most frequent first)
    sorted_colors = sorted(color_counts.items(), key=lambda x: x[1], reverse=True)

    # Get the RGB values of the most distinct colors
    distinct_colors = [
        kmeans.cluster_centers_[color[0]].astype(int) for color in sorted_colors
    ]

    return [f"#{r:02x}{g:02x}{b:02x}" for [r, g, b] in distinct_colors]


def process_directory(directory, gun_type):
    print(f"Processing {directory}")
    color_data = {}
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(".png"):
                print(f"---- {file}")
                file_path = os.path.join(root, file)
                colors = extract_distinct_colors(file_path)
                color_data[pathlib.Path(file).stem] = {
                    "type": gun_type,
                    "colors": colors,
                }
    return color_data


def main():
    directories = ["phantom", "vandal"]
    all_colors = {}

    for directory in directories:
        skin_dir = os.path.join("skins", directory)
        if os.path.exists(skin_dir):
            all_colors.update(process_directory(skin_dir, gun_type=directory))
        else:
            print(f"Directory '{directory}' does not exist.")

    # print(all_colors)
    with open("colors.json", "w") as json_file:
        json.dump(all_colors, json_file, indent=4)


if __name__ == "__main__":
    main()

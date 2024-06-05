import numpy as np 
import json
import argparse
from PIL import Image 


parser = argparse.ArgumentParser()
parser.add_argument('--gray', type=argparse.FileType('r'), help='A list representing a \
                    grayscale image')

args = parser.parse_args()
gray = args.gray 


# Read gray images
with open(f"{gray.name}") as infile:
    gray_img = json.load(infile)

img = Image.fromarray(np.array(gray_img))

# Display the image
img.show()
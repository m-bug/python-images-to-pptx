import os
from pptx import Presentation
from pptx.util import Inches

prs = Presentation()

# custum vars
PATH = "./friends/"
OUTPUT_FILE = "image_slideshow.pptx"

# coordination vars
left = top = Inches(1)
height = Inches(5.5)

for root, dirs, filenames in os.walk(PATH):
    for file in filenames:
        image_path = os.path.join(root, file)
        blank_slide_layout = prs.slide_layouts[6]
        slide = prs.slides.add_slide(blank_slide_layout)

        pic = slide.shapes.add_picture(image_path, left, top, height=height)

prs.save(OUTPUT_FILE)
"""
    This script removes the background from all images in a folder and saves them in a subfolder called rembg.
    The images are converted to png and saved in a subfolder called pngd.
    Then the background is removed and the images are saved in a subfolder called rembg.
    The images are renamed to the desired format specified in the month_year variable.
    This script requires the rembg library, the PIL library and the easygui library which can be installed with pip.
    The first time you run this script, you will get an error message that you need to download the rembg model,
    or it will be done automatically.

    credits to
"""

import os
from rembg import remove
from PIL import Image
import easygui as eg


# if you want to rename the files, set this to True, this is done after removing the background in one previous pass
rename = True

# set the month and year of the found items so that the found items can be named accordingly, the last digits being incremental (e.g. no_background_fundsache_sept_2023_0.png)
month_year = "sept_2023"

if __name__ == "__main__":
    directory = eg.diropenbox(msg="Select a folder to remove background", title="Select a folder")
    # convert all images in the folder (chosen in the GUI) to png and save them in a subfolder called pngd for further use. The redundant jpg files are not deleted, because I didn trust myself to not delete the wrong files.
    counter = 0
    os.mkdir(os.path.join(directory, "pngd"))
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        print(f"FOUND {filename}")
        if filename.endswith(".jpg"):
            print(f"CONVERTING {filename} TO pngd/{counter}.png")
            input_path = os.path.join(directory, filename)
            output_path = os.path.join(directory, "pngd", str(counter) + ".png")
            inputfile = Image.open(input_path)
            inputfile.save(output_path, "png")
            counter += 1
            continue
        else:
            continue
    # remove the background from all images in the pngd folder and save them in a subfolder called rembg
    os.mkdir(os.path.join(directory, "pngd", "rembg"))
    for file in os.listdir(os.path.join(directory, "pngd")):
        filename = os.fsdecode(file)
        print(f"REMOVING BACKGROUND FROM {filename}")
        if filename.endswith(".png"):
            input_path = os.path.join(directory, "pngd", filename)
            output_path = os.path.join(directory, "pngd", "rembg", filename)
            input = Image.open(input_path)
            output = remove(input)
            output.save(output_path)
            continue
        else:
            continue
    # here were name the files to the desired format specified in the month_year variable
    counter = 0
    for file in os.listdir(os.path.join(directory, "pngd", "rembg")):
        filename = os.fsdecode(file)
        print(f"RENAMING {filename} TO {'no_background_fundsache_sept_2023_' + str(counter)}.png")
        if filename.endswith(".png"):
            input_path = os.path.join(directory, "pngd", "rembg", filename)
            output_path = os.path.join(directory, "pngd", "rembg",
                                       "no_background_fundsache_" + month_year + "_" + str(counter) + ".png")
            os.rename(input_path, output_path)
            counter += 1
            continue
        else:
            continue

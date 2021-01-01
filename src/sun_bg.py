from PIL import Image
import os
import urllib.request

SUN_IMAGE_URL_NASA = "https://sdo.gsfc.nasa.gov/assets/img/latest/latest_4096_211193171.jpg"
IMAGE_WORKING_DIRECTORY = "bgs"
SOURCE_IMAGE_FILENAME = "source.jpg"


def download_image():
    global SUN_IMAGE_URL_NASA, IMAGE_WORKING_DIRECTORY, \
        SOURCE_IMAGE_FILENAME
    # Make the working directory for images
    # if it doesn't exist.
    if not os.path.exists(IMAGE_WORKING_DIRECTORY):
        os.makedirs(IMAGE_WORKING_DIRECTORY)
    # Download the image
    urllib.request.urlretrieve(
        SUN_IMAGE_URL_NASA, "{}/{}".format(IMAGE_WORKING_DIRECTORY, SOURCE_IMAGE_FILENAME))


def create_backgrounds():
    global IMAGE_WORKING_DIRECTORY, SOURCE_IMAGE_FILENAME
    # The source image is 4096x4096
    # Split it with PIL to make the 1920x1080 pieces for both monitors
    with Image.open("{}/{}".format(IMAGE_WORKING_DIRECTORY, SOURCE_IMAGE_FILENAME)) as image:
        # Crop the portion that makes up the left monitor
        monitor_left = (128, 1508, 2048, 2588)
        monitor_region_left = image.crop(monitor_left)
        # Crop the portion that makes up the right monitor
        monitor_right = (2048, 1508, 3968, 2588)
        monitor_region_right = image.crop(monitor_right)
        # Write the images to disk
        monitor_region_left.save(
            "{}/monitor_left.jpg".format(IMAGE_WORKING_DIRECTORY))
        monitor_region_right.save(
            "{}/monitor_right.jpg".format(IMAGE_WORKING_DIRECTORY))


def main():
    # Download the image from NASA
    download_image()
    # Create the Desktop wallpaper images
    create_backgrounds()


if __name__ == "__main__":
    main()

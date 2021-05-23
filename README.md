# ImageDownsizeProgram
Simple program that takes a large image file (1080p and up) and saves it in multiple, smaller resolution images files and stores it in the database, and lets the user download them to their machine based on a chosen resolution (original, 720p, 480p)

Some assumptions
output image follows standard resolution formats as follows
320p - 480x320
480p - Low-Resolution 720 x 480
720p - HD Ready or High Definition ready 1280 x 720
1080p - FHD or Full High Definition 1920 x 1080


The App will resize the image by creating a canvas element for each smaller image copy. The canvas element will have 720p, 480p, and 320p as the smaller resolutions. 
The image is then redrawn with the max_width being set to the resolution they're set to (i.e. 1280 px, 720px, 480px) and are then displayed to the webpage. 
The image is actually a file that can be stored in the database if properly coded to send DataURL objects to the backend, and not a compressed rendered image.
If the image is actually downloaded from the webpage it'll be the correct dimensions dictated by the canvas element.

Some improvements to do:
1) dynamically create number of images you can create given the file resolution (i.e. if given a 1440p, be able to create a 1080p resolution image
2) Actually upload the image files to the backend server to be stored in the database
3) find a way to not have to copy paste the onLoad function responsible for generating the smaller images










Draft Docs

setup

python -m venv env 			// you can use any name to replace "env"

cd ImgResize            // brings you to the app directory

pip install -r requirements.txt 	// installs django and other libraries used (to be changed when I actually use other libraries)

python manage.py makemigrations //sets up django database, database isn't actually used, but it's left there to make it easier to implement saving image files in the server in future updates

python manage.py migrate  // commits the database

python manage.py runserver

How to use:

1) Go to localhost http://localhost:8000/
2) upload an image, a sample 1920 * 1080 image is supplied in the root directory for convenience, but it can work with any image
3) click submit


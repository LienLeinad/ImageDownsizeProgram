# ImageDownsizeProgram
Simple program that takes a large image file (1080p and up) and saves it in multiple, smaller resolution images files and stores it in the database, and lets the user download them to their machine based on a chosen resolution (original, 720p, 480p)

Some assumptions
image follows standard resolution formats as follows

480p - Low-Resolution 720 x 480
720p - HD Ready or High Definition ready 1280 x 720
1080p - FHD or Full High Definition 1920 x 1080
1440p - QHD or Quad High Definition 2560 x 1440


1080p to 720p is 1080p * 4/9
720p to 480p is 1080p * 0.375
Image uploaded can be any of the given above, and output will be the lower resolutions below the given input
e.g. 
1440p upload will give you 1080p, 720p, and 480p on the database
1080p upload will give you 720p, 480p
720p upload will give you 480p
480p will just return the same image


if the file format does not follow standard formats, then the following formula will be used




Draft Docs

setup
python -m venv env 			// you can use any name to replace "env"
cd ImgResize            // brings you to the app directory
pip install -r requirements.txt 	// installs django and other libraries used (to be changed when I actually use other libraries)

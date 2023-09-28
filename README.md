# ImageProcessor

 A Django image processor, that allows for image-file upload, and storage and deletion. 
 The user will be able to upload a file image from the index page. Upon successful file upload, the user is redirected to a display images page where the user is able to see all of the uploads previously commited. In the image gallery displayed, there is a dropdown menu for each image with the following information: Image name, hex value, RGB value, color name, the option to remove the photo from the database, and a visual representation of the color with a link to more information about the color. 

As an extra initiative the code is hosted as a web app to view for those who don't want to run the repository locally. To view this please visit:
http://joshuaroelf.pythonanywhere.com/

Note: There is an error with the static files serving on the hosted web app so the background will just display as grey. 


 Set up instructions: 

1) clone the repo
2) set up your virtual environment ensuring python is version 3.11.4
3) run the command py -m pip install -r /path/to/requirements.txt.
4) run py manage.py makemigrations then py manage.py migrate
5) Finally, run the server with py manage.py runserver


How it works: 

This project uses PIL, webcolors, bootstrap5, to make all the wheels turn in our application. 

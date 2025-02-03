# Movie Character Filters 🎥

It happens often that when I watch Pride and Prejudice (2005) and see Fitzwilliam Darcy on the big screen that I can't help but feel a sense of melancholy: "*I wish I looked like a rich man with no social skills*"

Hold on....I can! 

So I took to my computer and performed some basic face detection using Haar Cascades to overlay images of my favorite movie characters onto my face. 

Here's how: 
* cam.py contains a basic rundown of detecting a face and placing an image of Edward Cullen onto it 
* filters.py generalizes this so I can overlay an image of the user's choice 
* my flask app contains a homescreen with all my favorite movies + their respective characters, the user can select a character and it takes them to another page which opens up the camera on their device and places an image of the chosen character onto their face

Next steps: 
* create cleaner image overlays
* more character choices
* polished UI
* hosting website on GitHub Pages
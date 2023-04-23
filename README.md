# Introduction
Blender addon that calculates the coordinates of the control points and handles of a Bezier curve and convert them into Whitehole coordinates through a .txt file. It's specifically made for the Tube Slide Controller.

# Requirements
In order to use this addon, you have to to follow some requirments:
* Your Slide model has to be imported in Whitehole and placed in your level
* Your Curve must be a Bezier. Nurbs curves aren't supported yet
* Your Curve must be scaled by 1000 (in order to match the game's real proportions) and rotated at -90° on the X axis
* You must apply all tranformations on the Curve (CTRL + A in Object Mode)

   ![Image](https://user-images.githubusercontent.com/74122269/228070054-b4aeabe8-73c4-4665-9d53-f576b32fd6ab.PNG)
   
This Add-on is 
 compatible with Blender 3.0> and 2.79<br /><br />

# Installation
Download the right version of the add-on and open Blender. Go to “Edit” in the Top Bar and choose “preferences”, select the tab labeled “Add-Ons”, click the “Install” button on the top right and select the downloaded file. Next, check on the box to the left of the  Add-on.

# How to use 
To access the Add-on's panel, go to the 3D-VIEW and press N. This will open a side panel on the right. After that, just click on the "Slide" tab.<br />

The panel is divided into 4 sections:
* The selection of the Bezier curve
* The coordinates of the 3D model of the slide in Whitehole
* The Output directory where the .txt file will be exported
* The button that makes the calculations
 
   ![Capture2](https://user-images.githubusercontent.com/74122269/228651087-9756faf1-cdcc-4468-a598-a51abefffa6f.PNG)

<br />For starters, into the first section select your Bezier curve . On the next section, copy the coordinated of your Slide model in Whitehole and paste them into the panel. Keep in mind that Whitehole uses commas for decimal numbers, this means that you have to delete every point and replace commas with points (e.g. 9.497,771 = 9497.771)
![Capture3](https://user-images.githubusercontent.com/74122269/228654851-ce325c55-7aa4-4e0e-bcd3-db25fd6df0b8.PNG)
 ![Capture4](https://user-images.githubusercontent.com/74122269/228654174-c8e10932-9c20-462c-88c7-b0e9beaee8cc.PNG)

On the third section, choose a file path in your pc where your .txt will be exported. When everything is set, press the "Print coordinates" button. You will receive the text file with the right coordinates immediatly. All you have to do now is open Whitehole again, and create your path for your slide with the new coordinates.


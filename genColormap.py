""" 
	Script for generating Colormap.XML files compatible with Paraview 
	...
	by Siddhartha Mukherjee, 6th of June, 2023 
	ICTS-TIFR, Bengaluru, India
"""
"""	
	Example usage:
	#-- Specify a name for the colormap
	cmapName 	= "Lava2" 
	#-- Provide a list of colours in hexadecimal, atleast 2, with or without the leading "#" (made consistent later)
	cols 		= ["03071e","6a040f","9d0208","d00000","e85d04","faa307","ffba08","fde7ae"]	

	Running this script will create and save "Lava2.xml" in a Folder called "Colormaps"

	Some nice Colormaps using palettes from https://coolors.co/:
	"WesAndy" 		: ["001219","005f73","0a9396","94d2bd","e9d8a6","ee9b00","ca6702","bb3e03","ae2012","9b2226"]
	"Aurora" 		: ["d9ed92","b5e48c","99d98c","76c893","52b69a","34a0a4","168aad","1a759f","1e6091","184e77"]
	"Lava" 			: ["03071e","370617","6a040f","9d0208","d00000","dc2f02","e85d04","f48c06","faa307","ffba08"]
	"Lapis" 		: ["05668d","028090","00a896","02c39a","#B5E7B5", "#D3EDB9"]
	"Aqua" 			: ["073b4c","00b4d8","b5e48c","ffe8d6"]

	Useful workflow when using the Coolors website:
	Start with https://coolors.co/palettes ->
	Select a palette and then "Open in Generator" (click on the three dots next to the palette) ->
	Tweak colours ->
	Export (Ctrl + E) -> Code -> Double click and copy the "Array" representation
	Paste the Array below, together with a name and run the script

	Tip: It is often nice to start with two simple colours and then add some intermediate/end shades. 
"""

from colormapFunctions import *

##-----------------------------------Enter Colormap----------------------------------------

cmapName        = "Lava2"
cols 			= ["03071e","6a040f","9d0208","d00000","e85d04","faa307","ffba08","fde7ae"]

##-----------------------------------------------------------------------------------------

cols            = [ "#"+c if "#" not in c else c for c in cols ] #-- Adding a "#" from habit, so the array is usable with matplotlib.pyplot
colormap   		= genColormapFromList(cmapName, cols)

#-- Or try a random Colormap - not very useful but sometimes fun and serendipitous!
# ncols 			= 10
# colormap  		= genColormapRandom(cmapName, ncols)

"""	
	Note on Paraview usage:
	Once a rendering is done, open the "Colormap selector" and "Load" the generated colormap.
	Depending on the version of Paraview, the new map may/may not show up immediately - latter if the current 
	colormaps in view are set to "Default". In this case, change "Default" to "All", which will show the new map
	towards the end. You can select and click on "Show this map in Default", when applying the colormap, to have 
	it show up front.

	In honour of the Hue-Manatee: https://tenor.com/view/manatee-rainbow-nature-joke-funny-gif-5660562
"""

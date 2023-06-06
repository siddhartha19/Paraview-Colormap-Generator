import random, os

def hex_to_rgb(hex_color):
    hex_color = hex_color.strip("#")
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    return r/255.0, g/255.0, b/255.0

def genColormapRandom(name, num_points):
    color_map = '<ColorMaps><ColorMap space="Lab" indexedLookup="false" group="Interlinked" name="%s">\n' % name

    for i in range(num_points):
        x           = round(i / (num_points - 1), 6)
        o           = 1
        r, g, b     = random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)
        point       = '\t<Point x="%f" o="%f" r="%f" g="%f" b="%f"/>\n' % (x, o, r, g, b)
        color_map   += point
    
    color_map += '</ColorMap></ColorMaps>'

    if not os.path.exists("Colormaps"):
        os.makedirs("Colormaps")

    #-- Write to file
    with open("Colormaps/%s.xml" % name, "w") as file:
        file.write(color_map)

    print("Colormap %s saved" % name)

    return color_map

def genColormapFromList(name, colsList):
    color_map = '<ColorMaps><ColorMap space="Lab" indexedLookup="false" group="Interlinked" name="%s">\n' % name
    
    for indx, c in enumerate(colsList):
        x           = indx*1.0/(len(colsList)-1.0)
        o           = 1
        r, g, b     = hex_to_rgb(c)
        point       = '\t<Point x="%f" o="%f" r="%f" g="%f" b="%f"/>\n' % (x, o, r, g, b)
        color_map   += point
    
    color_map += '</ColorMap></ColorMaps>'

    if not os.path.exists("Colormaps"):
        os.makedirs("Colormaps")

    #-- Write to file
    with open("Colormaps/%s.xml" % name, "w") as file:
        file.write(color_map)

    print("Colormap %s saved" % name)

    return color_map

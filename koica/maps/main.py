import folium
import os
import webbrowser
from pathlib import Path

def showMap(map_object):
    # 1. Save the map to an HTML file
    filename = "map.html"
    map_object.save(filename)
    
    # 2. Get the absolute path and convert it to a proper file:// URI
    filepath = Path(os.getcwd()) / filename
    file_uri = filepath.as_uri()
    
    # 3. Open it automatically in your default web browser
    webbrowser.open_new_tab(file_uri)

# Define location and create the map
loc = [9.311547, 123.299215]
my_map = folium.Map(location=loc, zoom_start=16 , tiles='CartoDB positron')

# Call the function to display it
showMap(my_map)
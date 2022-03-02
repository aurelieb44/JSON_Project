import json
infile = open('eq_data_1_day_m1.json', 'r')
outfile = open('readable_eq_data.json', 'w')

eq_data = json.load(infile) # convert the json file into a python object
json.dump(eq_data, outfile, indent=4) # takes the eq_data dictionary and creates a formatted json file so that we can read it

list_of_eqs = eq_data["features"] # list_of_eqs is a list of dictionaries

mags, lons, lats = [],[],[]

for eq in list_of_eqs: # going through each element in the dictionary and each element of the list is a dictionary
    mag = eq["properties"]["mag"]
    lon = eq["geometry"]["coordinates"][0]
    lat = eq["geometry"]["coordinates"][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
print(mags[:10])
print(lons[:10])
print(lats[:10])

print(len(list_of_eqs))

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [Scattergeo(lon=lons, lat=lats)] # those lon and lat are the arguments for the Scattergeo function, different from the variables in the for loop
# lats expects a list of latitudes # lons expects a list of longitudes
# extract data and put it in a format that we can use for a graph

my_layout = Layout(title='Global Earthquakes')
fig = {'data':data, 'layout':my_layout}
offline.plot(fig,filename='global_earthquakes.html')
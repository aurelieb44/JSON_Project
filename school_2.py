"""
Process the JSON file named univ.json. Create 3 maps per instructions below.
The size of the point on the map should be based on the size of total enrollment. Display only those schools 
that are part of the ACC, Big 12, Big Ten, Pac-12 and SEC divisons (refer to valueLabels.csv file) 
The school name and the specific map criteria should be displayed when you hover over it.
(For example for Map 1, when you hover over Baylor, it should display "Baylor University, 81%")
Choose appropriate tiles for each map.

Map 1) Graduation rate for Women is over 50%
Map 2) Percent of total enrollment that are Black or African American over 10%
Map 3) Total price for in-state students living off campus over $50,000
"""

import json
infile = open('univ.json', 'r')

list_of_univ = json.load(infile) # convert the json file into a python object

hover_texts, enrolls, lons, lats = [], [], [], []

for univ in list_of_univ:

    conf = int(univ["NCAA"]["NAIA conference number football (IC2020)"]) 

    if conf == 372 or conf == 108 or conf == 107 or conf == 127 or conf == 130 :

        if int(univ["Percent of total enrollment that are Black or African American (DRVEF2020)"])>10:
            lon=int(univ["Longitude location of institution (HD2020)"])
            lat=int(univ["Latitude location of institution (HD2020)"])
            lons.append(lon)
            lats.append(lat)
            enroll_aa=int(univ["Percent of total enrollment that are Black or African American (DRVEF2020)"])            
            institution=univ["instnm"]
            hover_text = institution + ', ' + str(enroll_aa) +'%'
            hover_texts.append(hover_text)
            enroll=univ["Total  enrollment (DRVEF2020)"]
            enrolls.append(enroll)

print(hover_texts[:10])
print(enrolls[:10])

from plotly.graph_objs import Scattergeo,Layout
from plotly import offline

data = [
    {'type':'scattergeo',
    'lon':lons,
    'lat':lats,
    'text':hover_texts, 
    'marker':{
        'size':[0.0005*enroll for enroll in enrolls], # bigger plots
        'color':enrolls,
        'colorscale':'Viridis',
        'reversescale':True, #darkest color is highest magnitude
        'colorbar':{'title':'Enrollment'}
    },
    }]

my_layout = Layout(title='% of African American Enrollment For ACC, Big 12, Big Ten, Pac-12 and SEC Universities')
fig = {'data':data, 'layout':my_layout}
offline.plot(fig,filename='african_american_enrollment.html')

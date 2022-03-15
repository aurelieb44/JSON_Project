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

        #if int(univ["Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"])>50000:
        if univ["Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"]: 
            if univ["Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"]>50000:
            
                try:
                    lon=int(univ["Longitude location of institution (HD2020)"])
                    lat=int(univ["Latitude location of institution (HD2020)"])
                    price_is_oc=int(univ["Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"])            
                    institution=univ["instnm"]
                    enroll=univ["Total  enrollment (DRVEF2020)"]
                
                except ValueError:  
                    print(f"Missing Data for {institution}") 
                
                else:
                    lons.append(lon)
                    lats.append(lat)
                    hover_text = institution + ', $' + str(price_is_oc) 
                    hover_texts.append(hover_text)
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
        'size':[0.0007*enroll for enroll in enrolls], # bigger plots
        'color':enrolls,
        'colorscale':'Viridis',
        'reversescale':True, #darkest color is highest magnitude
        'colorbar':{'title':'Enrollment'}
    },
    }]

my_layout = Layout(title='Price for in-state students living off campus For ACC, Big 12, Big Ten, Pac-12 and SEC Universities')
fig = {'data':data, 'layout':my_layout}
offline.plot(fig,filename='price_is_students_offcampus.html')

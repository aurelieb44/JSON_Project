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

grad_w, institutions, enrolls = [], [], []

for univ in list_of_univ:
    #print(type(int(univ['Graduation rate  women (DRVGR2020)'])))
    #print(type(50))
    #if int(univ['Graduation rate  women (DRVGR2020)'])>50:
        #grad_rate_w=int(univ['Graduation rate  women (DRVGR2020)'])
        #grad_w.append(grad_rate_w)
        institution=univ["instnm"]
        institutions.append(institution)
        enroll=univ["Total  enrollment (DRVEF2020)"]
        enrolls.append(enroll)

print(grad_w[:10])
print(institutions[:10])
print(enrolls[:10])

from plotly.graph_objs import Scattergeo,Layout
from plotly import offline

data = [
    {'type':'scattergeo',
    'grad_rate_w':grad_w,
    'institution':institution,
    'enrollment':enroll,
    'marker':{
        'size':[2*enroll for enroll in enrolls], # bigger plots
        'color':enrolls,
        'colorscale':'Viridis',
        'reversescale':True, #darkest color is highest magnitude
        'colorbar':{'title':'Enrollment'}
    },
    }]

my_layout = Layout(title='Graduation rate for Women over 50%')
fig = {'data':data, 'layout':my_layout}
offline.plot(fig,filename='graduation_rate_women.html')



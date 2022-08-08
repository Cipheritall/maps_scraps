# Definitions
import pandas as pd 
from bokeh.io import show
from bokeh.plotting import gmap
from bokeh.models import GMapOptions
from bokeh.models import ColumnDataSource
from bokeh.io import output_notebook

from bokeh.plotting import figure, output_file, save



from gmapi import * 
from config import *
from centers import *



# Processing Centers
city_exterms = get_extermes(city_high_left,city_height,city_width)
centers = get_centers(city_exterms[0],city_exterms[1])
centers
pd.DataFrame(centers).to_csv("output/last_centers.csv")


bokeh_centers = {}
bokeh_centers["lon"] = []
bokeh_centers["lat"] = []

for pos in centers:
    bokeh_centers["lat"].append(float(pos[0])) 
    bokeh_centers["lon"].append(float(pos[1])) 
df_bokeh_centers = pd.DataFrame(bokeh_centers)


# set output to static HTML file
output_file(filename="output/last_centers.html", title="Static HTML file")

#output_notebook()
bokeh_width, bokeh_height = 1000,1000

lat, lon = float(city_high_left[0]),float(city_high_left[1])

def plot(lat, lng, zoom=10, map_type='terrain'):
    gmap_options = GMapOptions(lat=lat, lng=lng, 
                               map_type=map_type, zoom=zoom)
    p = gmap(key, gmap_options, title='Pays de Gex', 
             width=bokeh_width, height=bokeh_height)
    df_bokeh_centers["radius"]=1
    source = ColumnDataSource(
        data=dict(lon=bokeh_centers["lon"],
                  lat=bokeh_centers["lat"])
    )
    # see how we specify the x and y columns as strings, 
    # and how to declare as a source the ColumnDataSource:
    center = p.circle('lon', 'lat', size=10, alpha=0.6, 
                      color='red', source=source)
    show(p)
    return p

p = plot(lat, lon)

if(input("Are you ok with the cucrrent coverage y/N : ") in ["Y","y","yes","oui"]):
    print("ok")
    raw = []
    center_index = 0
    for center in centers:
        print(f"Processing cercle {center_index}/{len(centers)}")
        out = scrap_n_business(business_total,center,float(radius)*np.sqrt(2),business_type,keyword)
        for business in out:
            raw.append(business)
        center_index += 1
    loot = pd.DataFrame(raw)
    loot.to_csv("output/last_loot.csv")
    now = datetime.datetime.now()
    filename = now.strftime('%y%m%d_%H_%M_%S_')
    filename = f"output/{city_name}_{business_type}_{filename}.xlsx"
    loot.to_excel(filename)
    print("#############################################################")
    print("#                        Final STEP                         #")
    print("# Download the Excel file from the dashboard in the left !  #")
    print(f"# Output file saved at : {filename} #")
    print("#############################################################")
else:
    print("aborted")
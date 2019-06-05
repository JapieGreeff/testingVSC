import geopandas as gpd
import fiona
import numpy as np 
#create a list of layers with in a file geodatabase 
db = 'Demographics.gdb'
layerlist = np.array(fiona.listlayers(db))
print(layerlist)
df = gpd.read_file(db, layer = 'GCRMunicipalities_surrounding_June2009_pop_prj')
print(df)
#for i in sorted(layerlist):
#    df1 = gpd.read_file('Demographics.gdb',layer=i)
#    print(df1)
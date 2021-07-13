import pandas as pd
import numpy as np
import geopandas as gpd
from shapely.geometry import Point, LineString, shape


def loadXY(id, polygon):
    x, y = polygon.exterior.coords.xy
    idx = np.full((len(x)), int(id))
    arr = np.array([idx, np.array(x), np.array(y)]).T
    df = pd.DataFrame(data=arr, columns=["storeid", "Latitude", "Longitude"])
    df = df.astype({'storeid': 'int32'})
    df.to_csv(f"./{id}.txt", index=False)


if __name__ == "__main__":
    path = '~/poly.geojson'
    df = gpd.read_file(path)

    ids = df['siteCode']
    polygons = df['geometry']

    for i in range(len(ids)):
        loadXY(ids[i], polygons[i][0])

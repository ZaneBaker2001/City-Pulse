import geopandas as gpd

def engineer_features(df):
    df['hour'] = df['datetime'].dt.hour
    df['dayofweek'] = df['datetime'].dt.dayofweek
    df['pm25_rolling'] = df['pm25'].rolling(window=3, min_periods=1).mean()
    return df

def add_geospatial_features(df, shapefile_path):
    gdf = gpd.read_file(shapefile_path)
    points = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.lon, df.lat), crs="EPSG:4326")
    joined = gpd.sjoin(points, gdf, how="left", predicate='intersects')
    df['district'] = joined['district_name']
    return df
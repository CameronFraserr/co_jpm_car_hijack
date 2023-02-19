import plotly.express as px

def plot_gps(filename):
    gps_points = []

    with open(filename) as f:
        for line in f.readlines():
            elements = line.strip().split(", ")
            gps_lat = float(elements[0])
            gps_lon = float(elements[1])
            gps_points.append((gps_lat, gps_lon))

    map_plot = px.line_mapbox(lat=[point[0] for point in gps_points], lon=[point[1] for point in gps_points], hover_name=None, hover_data=None, zoom=13, height=800)
    map_plot.update_layout(mapbox_style="open-street-map")
    map_plot.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    map_plot.show()

plot_gps("gps_transmissions_decoded.txt")
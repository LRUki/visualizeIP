class plotOnGMap():
    def __init__(self,countryDF,regionDF):
        self.country = countryDF
        self.region = regionDF
    def plotByCountries(self):
        from bokeh.io import output_file, show
        from bokeh.models import GMapPlot, GMapOptions, ColumnDataSource, Circle, Range1d, PanTool, WheelZoomTool, BoxSelectTool
        map_options = GMapOptions(lat=0, lng=0, zoom=3)
        plot = GMapPlot( x_range= Range1d(), y_range= Range1d(), map_options=map_options)
        plot.title.text = "Number of IP addresses by country"
        plot.api_key = "AIzaSyBhp55aOUd89Uj3KDP3cvbZJkeHviiA8Qc"
# Now we create a ColumnDataSource object and pass in the latitude 
# and longitude, and the number of IPV4 to have a differnet size of plots

        source = ColumnDataSource(
            data=dict(
                lats=list(self.country.latitude),
                lons=list(self.country.longitude),
                sizes=[(x**(1/2))/2 for x in self.country.numberOfIp]
            )
        )


        # Next we use the Circle()class to define how the points will look on the map:
    
        circle1 = Circle(x="lons", y="lats", size="sizes", fill_color="red", fill_alpha=0.35, line_color=None)
        plot.add_glyph(source, circle1)
        circle2 = Circle(x="lons", y="lats", size=3, fill_color="red", fill_alpha=1, line_color=None)
        plot.add_glyph(source,circle2)

        # Then we add the tools we want to use (Paning, Wheel Zoom, and general box selection)
        plot.add_tools(PanTool(), WheelZoomTool(), BoxSelectTool())

        # Now we show the plot (you should see a new tab or window open here)
        #output_file("Country_Ip.html")
        show(plot)
    def plotByRegions(self):
        from bokeh.io import output_file, show
        from bokeh.models import GMapPlot, GMapOptions, ColumnDataSource, Circle, Range1d, PanTool, WheelZoomTool, BoxSelectTool
        map_options = GMapOptions(lat=0, lng=0, zoom=3)
        plot = GMapPlot( x_range= Range1d(), y_range= Range1d(), map_options=map_options)
        plot.title.text = "Number of IP addresses by region"
        plot.api_key = "AIzaSyBhp55aOUd89Uj3KDP3cvbZJkeHviiA8Qc"
# Now we create a ColumnDataSource object and pass in the latitude 
# and longitude, and the number of IPV4 to have a differnet size of plots

        source = ColumnDataSource(
            data=dict(
                lats=list(self.region.latitude),
                lons=list(self.region.longitude),
                sizes=[(x**(1/2))/2 for x in self.region.numberOfIp]
            )
        )


        # Next we use the Circle()class to define how the points will look on the map:
    
        circle1 = Circle(x="lons", y="lats", size="sizes", fill_color="blue", fill_alpha=0.35, line_color=None)
        plot.add_glyph(source, circle1)
        circle2 = Circle(x="lons", y="lats", size=3, fill_color="blue", fill_alpha=1, line_color=None)
        plot.add_glyph(source,circle2)

        # Then we add the tools we want to use (Paning, Wheel Zoom, and general box selection)
        plot.add_tools(PanTool(), WheelZoomTool(), BoxSelectTool())

        # Now we show the plot (you should see a new tab or window open here)
        #output_file("Country_Ip.html")
        show(plot)



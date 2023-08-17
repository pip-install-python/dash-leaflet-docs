from dash_extensions.javascript import assign
from dash_extensions.enrich import DashProxy
from dash_leaflet import Map, TileLayer

eventHandlers = dict(
    click=assign("function(e, map, props){console.log(`You clicked at ${e.latlng}.`)}"),
)
app = DashProxy(__name__)
app.layout = Map(children=[TileLayer()], eventHandlers=eventHandlers,
                 style={'height': '50vh'}, center=[56, 10], zoom=6)

if __name__ == '__main__':
    app.run_server()

import dash
import dash_html_components as html
import dash_leaflet as dl

app = dash.Dash()
app.layout = html.Div([
    dl.Map([dl.TileLayer(),
            dl.MeasureControl(position="topleft", primaryLengthUnit="kilometers", primaryAreaUnit="hectares",
                              activeColor="#214097", completedColor="#972158")],
           style={'width': '100%', 'height': '50vh', 'margin': "auto", "display": "block"}),
])

if __name__ == '__main__':
    app.run_server(port=7778)

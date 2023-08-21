import dash_leaflet as dl
from dash_extensions.enrich import DashProxy
from dash_svg import Rect

bounds = [[56, 10], [55, 9]]
app = DashProxy()
app.layout = dl.Map([
    dl.TileLayer(),
    dl.SVGOverlay(
        children=[
            Rect(width=200, height=200),
            Rect(x=75, y=23, width=50, height=50, style="fill:red"),
            Rect(x=75, y=123, width=50, height=50, style="fill:#0013ff"),
        ],
        attributes=dict(
            stroke='red',
            viewbox="0 0 200 200",
            xmlns="http://www.w3.org/2000/svg"
        ), bounds=bounds,
    )
], center=[56, 10], zoom=6, style={'height': '50vh'})

if __name__ == '__main__':
    app.run_server()

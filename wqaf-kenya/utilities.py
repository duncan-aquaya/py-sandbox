

def county_shape_style(x):
    """Style KWDS:
    stroke: bool (default True) Outline
    color: string Stroke color
    weight: int Stroke width in pixels
    opacity: float (default 1.0) Stroke opacity
    fill: bool (default True) Whether to fill
    fillColor: str
    fillOpacity: float (default 0.5)
    """
    if x["properties"]["COUNTY_CLF"] == "primary":
        return dict(color="red", weight=2, opacity=0.75, fill=True, fillOpacity=0.05)
    elif x["properties"]["COUNTY_CLF"] == "secondary":
        return dict(color="orange", weight=2, opacity=0.75, fill=True, fillOpacity=0.05)
    else:
        return dict(stroke=False, fill=False)

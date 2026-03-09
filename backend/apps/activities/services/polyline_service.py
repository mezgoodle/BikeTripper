import polyline


def encode_polyline(points):
    """
    points: [(lat, lon), (lat, lon)]
    """
    return polyline.encode(points, precision=5)

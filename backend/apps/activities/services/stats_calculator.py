from math import radians, sin, cos, sqrt, atan2


def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371000

    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return R * c


def calculate_stats(points):
    """
    points: GPX points
    """

    total_distance = 0
    elevation_gain = 0
    prev_point = None

    for point in points:

        if prev_point:

            distance = calculate_distance(
                prev_point.latitude,
                prev_point.longitude,
                point.latitude,
                point.longitude,
            )

            total_distance += distance

            if point.elevation and prev_point.elevation:
                diff = point.elevation - prev_point.elevation
                if diff > 0:
                    elevation_gain += diff

        prev_point = point

    return total_distance, elevation_gain

from math import radians, sin, cos, sqrt, atan2

import gpxpy
import gpxpy.gpx


def calculate_distance(lat_1, lon_1, lat_2, lon_2) -> float:
    radius = 6371000

    lat_1 = radians(lat_1)
    lon_1 = radians(lon_1)
    lat_2 = radians(lat_2)
    lon_2 = radians(lon_2)

    d_lat = lat_2 - lat_1
    d_lon = lon_2 - lon_1

    a = sin(d_lat / 2) ** 2 + cos(lat_1) * cos(lat_2) * sin(d_lon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return radius * c


def parse_gpx(file):
    gpx = gpxpy.parse(file)

    total_distance = 0
    elevation_gain = 0

    points = []

    prev_point = None

    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:

                points.append((point.latitude, point.longitude))

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

    duration = 0

    if gpx.tracks:
        start = gpx.tracks[0].segments[0].points[0].time
        end = gpx.tracks[0].segments[0].points[-1].time

        if start and end:
            duration = (end - start).total_seconds()

    distance_km = total_distance / 1000

    avg_speed = 0

    if duration > 0:
        avg_speed = distance_km / (duration / 3600)

    polyline = ";".join([f"{lat},{lon}" for lat, lon in points])

    return {
        "distance_km": round(distance_km, 2),
        "duration_seconds": int(duration),
        "avg_speed": round(avg_speed, 2),
        "elevation_gain": round(elevation_gain, 2),
        "polyline": polyline,
    }

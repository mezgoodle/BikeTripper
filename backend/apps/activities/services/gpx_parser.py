import gpxpy

from .polyline_service import encode_polyline
from .stats_calculator import calculate_stats


def parse_gpx(file):
    """
    Parse GPX file and calculate ride statistics.

    Returns:
        dict:
            distance_km
            duration_seconds    
            avg_speed
            elevation_gain
            polyline
    """

    gpx = gpxpy.parse(file)

    all_points = []

    # Collect all GPX points
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                all_points.append(point)

    if not all_points:
        return None

    # Calculate distance and elevation
    distance, elevation = calculate_stats(all_points)

    # Calculate duration
    start_time = all_points[0].time
    end_time = all_points[-1].time

    duration = 0

    if start_time and end_time:
        duration = (end_time - start_time).total_seconds()

    # Convert distance to km
    distance_km = distance / 1000

    # Calculate average speed
    avg_speed = 0

    if duration > 0:
        avg_speed = distance_km / (duration / 3600)

    # Build encoded polyline
    coords = [(p.latitude, p.longitude) for p in all_points]
    encoded_polyline = encode_polyline(coords)

    return {
        "distance_km": round(distance_km, 2),
        "duration_seconds": int(duration),
        "avg_speed": round(avg_speed, 2),
        "elevation_gain": round(elevation, 2),
        "polyline": encoded_polyline,
    }

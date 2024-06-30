import math

# Function to convert degrees to radians
def degrees_to_radians(degrees):
    return degrees * math.pi / 180

# Function to parse and convert coordinates
def parse_coordinate(coord_str):
    try:
        # Strip whitespace and split the string by space
        value_str, direction = coord_str.strip().split()
        value = float(value_str.replace('°', ''))
        
        # Convert to degrees
        if direction in ['N', 'E']:
            return value
        elif direction in ['S', 'W']:
            return -value
        else:
            raise ValueError("Direction must be N, S, E, or W.")
    except ValueError as e:
        print(f"Error: {e}")
        return None

# Function to calculate distance using the haversine formula
def haversine(lon1, lat1, lon2, lat2, radius):
    lon1, lat1, lon2, lat2 = map(degrees_to_radians, [lon1, lat1, lon2, lat2])
    
    dlon, dlat = lon2 - lon1, lat2 - lat1
    
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    return radius * c

# Radius of the Moon in kilometers
moon_radius = 1737.4

# Function to input and validate coordinates
def get_coordinates(prompt):
    while True:
        coord = input(prompt)
        parsed_coord = parse_coordinate(coord)
        if parsed_coord is not None:
            return parsed_coord

print("Enter coordinates in the format 'value° N/S/E/W'.")

lon1 = get_coordinates("Longitude of the first point: ")
lat1 = get_coordinates("Latitude of the first point: ")
lon2 = get_coordinates("Longitude of the second point: ")
lat2 = get_coordinates("Latitude of the second point: ")

distance = haversine(lon1, lat1, lon2, lat2, moon_radius)

print(f"Distance between the points: {distance:.2f} km")

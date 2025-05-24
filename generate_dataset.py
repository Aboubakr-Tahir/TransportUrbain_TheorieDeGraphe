import csv
import random
import os

# Parameters for the synthetic dataset
num_stations = 50
min_connections = 2
max_connections = 5
min_distance = 0.5  # km
max_distance = 10.0  # km
min_passengers = 50  # passengers per day
max_passengers = 2000  # passengers per day

# Create data directory if it doesn't exist
os.makedirs('data', exist_ok=True)

# Generate station data
stations = []
for i in range(1, num_stations + 1):
    station_id = f"S{i}"
    station_name = f"Station {i}"
    # Generate random coordinates (simplified as x,y coordinates)
    x_coord = round(random.uniform(0, 50), 6)
    y_coord = round(random.uniform(0, 50), 6)
    station_type = random.choice(["Metro", "Bus", "Tram"])
    # Add station to list
    stations.append({
        "id": station_id,
        "name": station_name,
        "x_coord": x_coord,
        "y_coord": y_coord,
        "type": station_type
    })

# Save stations to CSV
with open('data/stations.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["StationID", "Name", "X_Coordinate", "Y_Coordinate", "Type"])
    for station in stations:
        writer.writerow([
            station["id"], 
            station["name"], 
            station["x_coord"], 
            station["y_coord"],
            station["type"]
        ])

# Generate connections between stations
connections = []
station_ids = [station["id"] for station in stations]

for station in stations:
    # Randomly decide how many connections this station will have
    num_connections = random.randint(min_connections, max_connections)
    # Get potential target stations (excluding self)
    potential_targets = [s_id for s_id in station_ids if s_id != station["id"]]
    # Ensure we don't exceed the available targets
    num_connections = min(num_connections, len(potential_targets))
    # Randomly select target stations
    target_stations = random.sample(potential_targets, num_connections)
    
    for target in target_stations:
        # Generate a random distance
        distance = round(random.uniform(min_distance, max_distance), 2)
        # Generate random passenger data
        passengers = random.randint(min_passengers, max_passengers)
        # Add connection
        connections.append({
            "source": station["id"],
            "target": target,
            "distance": distance,
            "passengers": passengers
        })

# Remove duplicate connections (if A→B exists, we don't need B→A)
unique_connections = []
connection_pairs = set()

for conn in connections:
    # Create a normalized pair (always smaller ID first)
    sorted_pair = tuple(sorted([conn["source"], conn["target"]]))
    
    if sorted_pair not in connection_pairs:
        connection_pairs.add(sorted_pair)
        unique_connections.append(conn)

# Save connections to CSV
with open('data/connections.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["SourceStationID", "TargetStationID", "Distance_km", "DailyPassengers"])
    for conn in unique_connections:
        writer.writerow([
            conn["source"], 
            conn["target"], 
            conn["distance"],
            conn["passengers"]
        ])

print(f"Generated {len(stations)} stations and {len(unique_connections)} connections.")
print("Data saved to 'data/stations.csv' and 'data/connections.csv'.")
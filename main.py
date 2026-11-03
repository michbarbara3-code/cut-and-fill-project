import csv
import matplotlib.pyplot as plt

# --- PART 1: READ THE CSV FILE ---
stations = []

with open('sample_stations.csv', mode='r') as file:
    reader = csv.reader(file)
    next(reader) # Skips the header row
    
    for row in reader:
        chainage = float(row[0])
        cut = float(row[1])
        fill = float(row[2])
        stations.append([chainage, cut, fill])

# --- PART 2: DO THE MATH & MASS HAUL ---
print("--- Earthwork Volume Report ---")

total_cut = 0.0
total_fill = 0.0
mass_haul = 0.0

plot_chainages = []
plot_mass_haul = []

for i in range(len(stations) - 1):
    station1 = stations[i]
    station2 = stations[i + 1]
    
    L = station2[0] - station1[0]
    
    cut_volume = (L / 2) * (station1[1] + station2[1])
    fill_volume = (L / 2) * (station1[2] + station2[2])
    
    total_cut += cut_volume
    total_fill += fill_volume
    
    net = cut_volume - fill_volume
    mass_haul += net
    
    plot_chainages.append(station2[0])
    plot_mass_haul.append(mass_haul)
    
    print(f"Chainage {station2[0]} -> Cut: {cut_volume:.2f} | Fill: {fill_volume:.2f} | Mass Haul: {mass_haul:.2f}")

print(f"\nTotal Cut: {total_cut:.2f}")
print(f"Total Fill: {total_fill:.2f}")

# --- PART 3: DRAW THE GRAPH ---
plt.figure(figsize=(8, 5)) 
plt.plot(plot_chainages, plot_mass_haul, marker='o', color='blue', linestyle='-')

plt.title("Mass Haul Diagram")
plt.xlabel("Chainage (m)")
plt.ylabel("Cumulative Volume (m3)")
plt.grid(True) 

plt.show()

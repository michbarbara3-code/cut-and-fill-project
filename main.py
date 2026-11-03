import csv
import matplotlib.pyplot as plt

# Read the data from the csv file
stations = []
with open('sample_stations.csv', mode='r') as file:
    reader = csv.reader(file)
    next(reader) # skip the header
    
    for row in reader:
        chainage = float(row[0])
        cut = float(row[1])
        fill = float(row[2])
        stations.append([chainage, cut, fill])

print("=" * 65)
print("                  EARTHWORK VOLUME REPORT")
print("=" * 65)
print(f"{'Chainage':<10} | {'Cut Vol':<10} | {'Fill Vol':<10} | {'Mass Haul'}")
print("-" * 65)

total_cut = 0
total_fill = 0
mass_haul = 0

x_values = []
y_values = []

for i in range(len(stations) - 1):
    s1 = stations[i]
    s2 = stations[i + 1]
    
    distance = s2[0] - s1[0]
    
    # End Area Method formula
    cut_vol = (distance / 2) * (s1[1] + s2[1])
    fill_vol = (distance / 2) * (s1[2] + s2[2])
    
    total_cut = total_cut + cut_vol
    total_fill = total_fill + fill_vol
    
    # Mass Haul is cut minus fill, added to the running total
    net = cut_vol - fill_vol
    mass_haul = mass_haul + net
    
    x_values.append(s2[0])
    y_values.append(mass_haul)
    
    # Print the results for this section with clean formatting
    print(f"Ch {int(s2[0]):<7} | {cut_vol:<10.2f} | {fill_vol:<10.2f} | {mass_haul:.2f}")

print("-" * 65)
print(f"TOTAL CUT VOLUME:  {total_cut:.2f} m3")
print(f"TOTAL FILL VOLUME: {total_fill:.2f} m3")
print(f"FINAL MASS HAUL:   {mass_haul:.2f} m3")
print("=" * 65)

# Draw the graph
plt.plot(x_values, y_values, marker='o')
plt.title("Mass Haul Diagram")
plt.xlabel("Chainage")
plt.ylabel("Volume")
plt.show()

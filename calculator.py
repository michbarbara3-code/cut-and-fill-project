# Survey data: [chainage, cut_area, fill_area]
stations = [
    [0, 10, 0],
    [50, 20, 0],
    [100, 0, 15],
    [150, 5, 0]
]

print("--- Cut and Fill Results ---")

total_cut = 0
total_fill = 0
cumulative_volume = 0  # <--- We start our running total at zero here

# Loop through the stations
for i in range(len(stations) - 1):
    
    station1 = stations[i]
    station2 = stations[i + 1]
    
    # L = distance between chainages
    L = station2[0] - station1[0]
    
    # End-Area Method
    cut_volume = (L / 2) * (station1[1] + station2[1])
    fill_volume = (L / 2) * (station1[2] + station2[2])
    
    total_cut = total_cut + cut_volume
    total_fill = total_fill + fill_volume
    
    # --- MASS HAUL LOGIC ---
    # This MUST be inside the loop so it happens for every section
    net = cut_volume - fill_volume
    cumulative_volume = cumulative_volume + net
    
    print("Section", i, "-> Cut:", cut_volume, "| Fill:", fill_volume)

print("-----------------------------")
print("Total Cut Volume:", total_cut)
print("Total Fill Volume:", total_fill)
print("Final Mass Haul Ordinate (Cumulative Net):", cumulative_volume)

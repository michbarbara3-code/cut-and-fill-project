import plotly.graph_objects as go

print("--- Cut and Fill Calculator ---")

# 1. MAKE IT INTERACTIVE
stations = []
print("Enter station data. Type 'done' when finished.\n")

while True:
    chainage_input = input("Enter Chainage (or type 'done'): ")
    
    if chainage_input.lower() == 'done':
        break
        
    cut_input = input("Enter Cut Area: ")
    fill_input = input("Enter Fill Area: ")
    
    stations.append([float(chainage_input), float(cut_input), float(fill_input)])
    print("Station added!\n")

if len(stations) < 2:
    print("You need at least 2 stations to calculate volume. Run the program again.")
else:
    # 2. THE MATH LOGIC
    total_cut = 0
    total_fill = 0
    cumulative_volume = 0 
    
    plot_chainages = [stations[0][0]] 
    plot_cumulative = [0]             

    print("\n--- Cut and Fill Results ---")
    
    for i in range(len(stations) - 1):
        station1 = stations[i]
        station2 = stations[i + 1]
        
        L = station2[0] - station1[0]
        
        cut_volume = (L / 2) * (station1[1] + station2[1])
        fill_volume = (L / 2) * (station1[2] + station2[2])
        
        total_cut += cut_volume
        total_fill += fill_volume
        
        net = cut_volume - fill_volume
        cumulative_volume += net
        
        plot_chainages.append(station2[0])
        plot_cumulative.append(cumulative_volume)
        
        print(f"Section {i} -> Cut: {cut_volume:.2f} | Fill: {fill_volume:.2f}")

    print("-" * 30)
    print(f"Total Cut Volume: {total_cut:.2f}")
    print(f"Total Fill Volume: {total_fill:.2f}")
    print(f"Final Mass Haul Ordinate: {cumulative_volume:.2f}")

    # 3. DRAW THE MASS HAUL DIAGRAM WITH PLOTLY
    print("\nGenerating Interactive Mass Haul Diagram...")
    
    # Create the figure
    fig = go.Figure()

    # Add your cumulative volume line
    fig.add_trace(go.Scatter(
        x=plot_chainages, 
        y=plot_cumulative, 
        mode='lines+markers', 
        name='Mass Haul Ordinate',
        line=dict(color='blue', width=3),
        marker=dict(size=8)
    ))

    # Add a dashed zero line
    fig.add_hline(y=0, line_dash="dash", line_color="black", annotation_text="Zero Line")

    # Update the layout (titles, etc.)
    fig.update_layout(
        title='Interactive Mass Haul Diagram',
        xaxis_title='Chainage (m)',
        yaxis_title='Cumulative Volume (m³)',
        hovermode='x unified', # This makes the hover tooltip look really nice
        template='plotly_white' # Gives it a clean, professional look
    )

    # Show the graph in your browser!
    fig.show()
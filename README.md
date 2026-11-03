# Cut and Fill Volume Calculator with Mass Haul Analysis

**Group 8 Coursework Project**

## Description
This program calculates earthwork volumes (Cut and Fill) between survey stations using the End-Area Method. It reads station data from a CSV file, calculates the cumulative Mass Haul (net soil movement), and plots a Mass Haul Diagram using Matplotlib.

## How to Run the Program
1. Ensure Python 3 is installed on your computer.
2. Open the terminal and install the required graphing library by typing:
   `pip install matplotlib`
3. Make sure the `sample_stations.csv` file is in the same folder as `main.py`.
4. Run the `main.py` script. 
5. The program will print the volume report in the terminal and display a graph window.

## Input Data Format
The program reads data from `sample_stations.csv`. The data is a standard textbook verification example and is formatted as:
- Chainage (m)
- Cut Area (m2)
- Fill Area (m2)

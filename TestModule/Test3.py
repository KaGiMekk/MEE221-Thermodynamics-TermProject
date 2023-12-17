import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
data = pd.read_csv('D:/SON/University/3rd Semester Sophomore/MEE221 Thermodynamics/FinalProject/DWSIM/Result/Original_Result.csv')

# Filter out the required states (assuming states 10, 11, 12, 13 exist)
states = [10, 11, 12, 13, 10]  # Repeat state 10 to close the cycle
cycle_data = data[data['State'].isin(states)]

# Plotting the T-s diagram
plt.figure(figsize=(10, 6))
plt.plot(cycle_data['Entropy'], cycle_data['Temperature'], marker='o')

# Adding labels and title
plt.xlabel('Entropy (s)')
plt.ylabel('Temperature (T)')
plt.title('T-s Diagram of the Organic Rankine Cycle')
plt.grid(True)

# Show the plot
plt.show()

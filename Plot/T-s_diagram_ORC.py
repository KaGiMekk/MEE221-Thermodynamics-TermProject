import numpy as np
import matplotlib.pyplot as plt
from CoolProp.CoolProp import PropsSI
import pandas as pd

# Define the fluids and their mass fractions
fluid1 = 'Isopentane'
fluid2 = 'R142b'
fraction1 = 0.3
fraction2 = 0.7

# Get Tmin and Tcrit for each fluid
T_min1 = PropsSI('Tmin', fluid1)
T_min2 = PropsSI('Tmin', fluid2)
T_crit1 = PropsSI('Tcrit', fluid1)
T_crit2 = PropsSI('Tcrit', fluid2)

# Use the higher Tmin and the lower Tcrit for the range
T_min = max(T_min1, T_min2)
T_crit = min(T_crit1, T_crit2)

temperatures = np.linspace(T_min, T_crit, 1000)

# Arrays to store entropy values for the mixture
s_liquid_mix = []
s_vapor_mix = []

# Calculate saturation properties for each component and combine them
for T in temperatures:
    s_l1 = PropsSI('S', 'T', T, 'Q', 0, fluid1)
    s_v1 = PropsSI('S', 'T', T, 'Q', 1, fluid1)
    s_l2 = PropsSI('S', 'T', T, 'Q', 0, fluid2)
    s_v2 = PropsSI('S', 'T', T, 'Q', 1, fluid2)

    # Combine the entropies based on mass fractions
    s_l_mix = (fraction1 * s_l1 + fraction2 * s_l2)/1000
    s_v_mix = (fraction1 * s_v1 + fraction2 * s_v2)/1000

    s_liquid_mix.append(s_l_mix)
    s_vapor_mix.append(s_v_mix)

# Calculate Process path
# Load the CSV file
file_path = r'D:\SON\University\3rd Semester Sophomore\MEE221 Thermodynamics\FinalProject\DWSIM\Result\Original_Result.csv'
data = pd.read_csv(file_path)
read_data = data.loc[9:12, ['Temperature', 'Pressure', 'Entropy']].values

#Calculate Saturation point in Process path
s_satliquid1 = PropsSI('S', 'P', 1890*1000, 'Q', 0, fluid1)
s_satliquid2 = PropsSI('S', 'P', 1890*1000, 'Q', 0, fluid2)
s_satliquid_mix = (fraction1 * s_satliquid1 + fraction2 * s_satliquid2)/1000

T_satliquid1 = PropsSI('T', 'P', 1890*1000, 'Q', 0, fluid1)
T_satliquid2 = PropsSI('T', 'P', 1890*1000, 'Q', 0, fluid2)
T_satliquid_mix = (fraction1 * T_satliquid1 + fraction2 * T_satliquid2)

s_satvapor1 = PropsSI('S', 'P', read_data[2,1]*1000, 'Q', 1, fluid1)
s_satvapor2 = PropsSI('S', 'P', read_data[2,1]*1000, 'Q', 1, fluid2)
s_satvapor_mix = (fraction1 * s_satvapor1 + fraction2 * s_satvapor2)/1000

T_satvapor1 = PropsSI('T', 'P', read_data[2,1]*1000, 'Q', 1, fluid1)
T_satvapor2 = PropsSI('T', 'P', read_data[2,1]*1000, 'Q', 1, fluid2)
T_satvapor_mix = (fraction1 * T_satvapor1 + fraction2 * T_satvapor2)

entropy_state = [read_data[0,2], s_satliquid_mix, read_data[1,2], read_data[2,2], s_satvapor_mix, read_data[3,2]]
temp_state = [read_data[0,0], T_satliquid_mix, read_data[1,0], read_data[2,0], T_satvapor_mix, read_data[3,0]]

# Plotting
plt.figure(figsize=(8, 6))
plt.plot(s_liquid_mix, temperatures, 'b', label='Saturation Liquid')
plt.plot(s_vapor_mix, temperatures, 'r', label='Saturation Vapor')

# Plot process path with points
plt.plot(entropy_state, temp_state, 'g-o', label='Process Path')

for i in range(len(entropy_state) - 1):
    plt.annotate('',
                 xy=(entropy_state[i+1], temp_state[i+1]),
                 xytext=(entropy_state[i], temp_state[i]),
                 arrowprops=dict(facecolor='green', shrink=0.05))

plt.annotate('',
             xy=(entropy_state[0], temp_state[0]),
             xytext=(entropy_state[-1], temp_state[-1]),
             arrowprops=dict(facecolor='green', shrink=0.05))

# Draw line to close the loop from the last state to the initial state
plt.plot([entropy_state[-1], entropy_state[0]], [temp_state[-1], temp_state[0]],'g')

plt.title('Approximate T-s Diagram for Isopentane/R142b Mixture (0.3/0.7 Mass Fraction)')
plt.xlabel('Entropy (KJ/kg.K)')
plt.ylabel('Temperature (K)')
plt.legend()
plt.grid(True)
plt.show()
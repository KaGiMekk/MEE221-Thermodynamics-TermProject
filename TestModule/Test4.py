import numpy as np
import matplotlib.pyplot as plt
from CoolProp.CoolProp import PropsSI

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

temperatures = np.linspace(T_min, T_crit, 100)

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
    s_l_mix = fraction1 * s_l1 + fraction2 * s_l2
    s_v_mix = fraction1 * s_v1 + fraction2 * s_v2

    s_liquid_mix.append(s_l_mix)
    s_vapor_mix.append(s_v_mix)

# Starting temperature
T_start = 305  # K

# Get saturation pressure at T_start for each component
P_sat1 = PropsSI('P', 'T', T_start, 'Q', 0, fluid1)
P_sat2 = PropsSI('P', 'T', T_start, 'Q', 0, fluid2)

# Calculate weighted average saturation pressure for the mixture
P_sat_mixture = fraction1 * P_sat1 + fraction2 * P_sat2

# Define the temperature range
T_min = T_start
T_max = min(PropsSI('Tcrit', fluid1), PropsSI('Tcrit', fluid2))
temperatures = np.linspace(T_min, T_max, 100)

# Arrays to store entropy values for the mixture at constant pressure
s_mix = []

# Calculate saturation properties for each component at constant pressure and combine them
for T in temperatures:
    s1 = PropsSI('S', 'P', P_sat_mixture, 'T', T, fluid1)
    s2 = PropsSI('S', 'P', P_sat_mixture, 'T', T, fluid2)

    # Combine the entropies based on mass fractions
    s_mixture = fraction1 * s1 + fraction2 * s2
    s_mix.append(s_mixture)

# Plotting
plt.figure(figsize=(8, 6))
plt.plot(s_mix, temperatures, label=f'Constant Pressure Line at {P_sat_mixture:.2f} Pa')
plt.plot(s_liquid_mix, temperatures, 'b', label='Liquid Line')
plt.plot(s_vapor_mix, temperatures, 'r', label='Vapor Line')
plt.xlabel('Entropy [J/(kg·K)]')
plt.ylabel('Temperature [K]')
plt.title('T-s Diagram for Isopentane/R142b Mixture (0.3/0.7)')
plt.legend()
plt.grid(True)
plt.show()

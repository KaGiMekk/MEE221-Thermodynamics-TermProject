import numpy as np
import matplotlib.pyplot as plt
from CoolProp.CoolProp import PropsSI
import pandas as pd

# Define the fluids and their mass fractions
fluid1 = 'Isobutane'
fluid2 = 'Pentane'
fraction1 = 0.8
fraction2 = 0.2

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

file_path = r'D:\SON\University\3rd Semester Sophomore\MEE221 Thermodynamics\FinalProject\DWSIM\Result\Original_Result.csv'
data = pd.read_csv(file_path)
read_data = data.loc[13:20, ['Temperature', 'Pressure', 'Entropy']].values

#state 14 > 14(sat_liq) > 15 > 15a > mo > 16 > 16(sat_vapor) > 17,18,19 > 20 > 21 > 21a
#state 14(sat_liq)
s_satliquid_14_1 = PropsSI('S', 'P', 904.35*1000, 'Q', 0, fluid1)
s_satliquid_14_2 = PropsSI('S', 'P', 904.35*1000, 'Q', 0, fluid2)
s_satliquid_14_mix = (fraction1 * s_satliquid_14_1 + fraction2 * s_satliquid_14_2)/1000

T_satliquid_14_1 = PropsSI('T', 'P', 904.35*1000, 'Q', 0, fluid1)
T_satliquid_14_2 = PropsSI('T', 'P', 904.35*1000, 'Q', 0, fluid2)
T_satliquid_14_mix = (fraction1 * T_satliquid_14_1 + fraction2 * T_satliquid_14_2)

#state 16(sat_vapor)
s_satvapor_16_1 = PropsSI('S', 'P', 348.55*1000, 'Q', 1, fluid1)
s_satvapor_16_2 = PropsSI('S', 'P', 348.55*1000, 'Q', 1, fluid2)
s_satvapor_16_mix = (fraction1 * s_satvapor_16_1 + fraction2 * s_satvapor_16_2)/1000

T_satvapor_16_1 = PropsSI('T', 'P', 348.55*1000, 'Q', 1, fluid1)
T_satvapor_16_2 = PropsSI('T', 'P', 348.55*1000, 'Q', 1, fluid2)
T_satvapor_16_mix = (fraction1 * T_satvapor_16_1 + fraction2 * T_satvapor_16_2)

entropy_state = [1.0915, s_satliquid_14_mix, 2.1987, 2.3221, s_satvapor_16_mix, 1.0876, 1.1106, 2.1323]
temp_state = [306.79, T_satliquid_14_mix, 356.26, 327.77, T_satvapor_16_mix, 306.32, 271.69, 271.69]

# Plotting
plt.figure(figsize=(8, 6))
plt.plot(s_liquid_mix, temperatures, 'b', label='Saturation Liquid')
plt.plot(s_vapor_mix, temperatures, 'r', label='Saturation Vapor')
plt.plot(entropy_state, temp_state, 'g-o', label='Process path')
plt.plot([entropy_state[7], entropy_state[3]], [temp_state[7], temp_state[3]], 'g')
plt.plot([entropy_state[5], entropy_state[0]], [temp_state[5], temp_state[0]], 'g')

for i in range(len(entropy_state) - 1):
    plt.annotate('',
                 xy=(entropy_state[i+1], temp_state[i+1]),
                 xytext=(entropy_state[i], temp_state[i]),
                 arrowprops=dict(facecolor='green', shrink=0.05))
    
plt.annotate('',
             xy=(entropy_state[3], temp_state[3]),
             xytext=(entropy_state[7], temp_state[7]),
             arrowprops=dict(facecolor='green', shrink=0.05))

plt.annotate('',
             xy=(entropy_state[0], temp_state[0]),
             xytext=(entropy_state[5], temp_state[5]),
             arrowprops=dict(facecolor='green', shrink=0.05))

# for i, (s, t) in enumerate(zip(entropy_state, temp_state), start=1):
#     plt.text(s, t, f' {i}', verticalalignment='bottom', horizontalalignment='right')

plt.title('Approximate T-s Diagram for Isobutane/Pentane Mixture (0.8/0.2 Mass Fraction)')
plt.xlabel('Entropy (kJ/kg.K)')
plt.ylabel('Temperature (K)')
plt.legend()
plt.grid(True)
plt.show()

# print(entropy_state)
# print(temp_state)

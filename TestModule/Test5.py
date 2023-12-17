import CoolProp.CoolProp as CP
import matplotlib.pyplot as plt
import numpy as np

# Define the working fluid and cycle parameters
fluid = 'R134a'  # Example organic fluid
T_evap = 80 + 273.15  # Evaporation temperature in Kelvin
T_cond = 30 + 273.15  # Condensation temperature in Kelvin
P_evap = CP.PropsSI('P', 'T', T_evap, 'Q', 1, fluid)
P_cond = CP.PropsSI('P', 'T', T_cond, 'Q', 0, fluid)

# Calculate state points
h1 = CP.PropsSI('H', 'P', P_evap, 'Q', 1, fluid)  # Enthalpy at state 1 (end of evaporation)
s1 = CP.PropsSI('S', 'P', P_evap, 'Q', 1, fluid)  # Entropy at state 1
h2 = CP.PropsSI('H', 'P', P_cond, 'S', s1, fluid)  # Enthalpy at state 2 (isentropic expansion)
h3 = CP.PropsSI('H', 'P', P_cond, 'Q', 0, fluid)  # Enthalpy at state 3 (end of condensation)
h4 = CP.PropsSI('H', 'P', P_evap, 'H', h3, fluid)  # Enthalpy at state 4 (isentropic compression)

# Create T-s plot
s = np.linspace(CP.PropsSI('S', 'P', P_cond, 'Q', 0, fluid), CP.PropsSI('S', 'P', P_evap, 'Q', 1, fluid), 100)
T = CP.PropsSI('T', 'P', P_evap, 'S', s, fluid)
plt.plot(s, T, label='T-s Diagram')
plt.plot([s1, s1], [T_cond, T_evap], 'r--', label='Isentropic Expansion')
plt.xlabel('Entropy (J/kg.K)')
plt.ylabel('Temperature (K)')
plt.legend()
plt.title('Organic Rankine Cycle (ORC) T-s Diagram')
plt.show()

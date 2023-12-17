import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Given data points for the liquid and vapor lines
# These are example data points and should be replaced with actual data
liquid_s = np.array([0, 500, 1000])
liquid_T = np.array([150, 250, 350])
vapor_s = np.array([1500, 1750, 2000])
vapor_T = np.array([150, 300, 400])

# Interpolating the liquid and vapor lines using a quadratic spline
liquid_interp = interp1d(liquid_s, liquid_T, kind='quadratic')
vapor_interp = interp1d(vapor_s, vapor_T, kind='quadratic')

# Generating more points for a smooth curve
s_fine_liquid = np.linspace(min(liquid_s), max(liquid_s), 500)
T_fine_liquid = liquid_interp(s_fine_liquid)

s_fine_vapor = np.linspace(min(vapor_s), max(vapor_s), 500)
T_fine_vapor = vapor_interp(s_fine_vapor)

# Plotting the interpolated curves
plt.figure(figsize=(8, 6))
plt.plot(s_fine_liquid, T_fine_liquid, 'b', label='Liquid Line (Interpolated)')
plt.plot(s_fine_vapor, T_fine_vapor, 'r', label='Vapor Line (Interpolated)')

# Filling the area between the curves
plt.fill_betweenx(T_fine_liquid, s_fine_liquid, s_fine_vapor, color='grey', alpha=0.3)

# Adding the title and labels
plt.title('Approximate T-s Diagram for Isopentane/R142b Mixture (0.3/0.7 Mass Fraction)')
plt.xlabel('Entropy (J/kg.K)')
plt.ylabel('Temperature (K)')
plt.legend()
plt.grid(True)
plt.show()

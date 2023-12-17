import pandas as pd
import CoolProp.CoolProp as CP

# Load the CSV file
file_path = r'D:\SON\University\3rd Semester Sophomore\MEE221 Thermodynamics\FinalProject\DWSIM\Result\Original_Result.csv'
data = pd.read_csv(file_path)

# Extracting pressure data for states 10 to 13
state_data = data.loc[9:12, 'Pressure']  # Assuming 'Pressure' column exists

# Constants
fluid1 = 'Isopentane'
fluid2 = 'R142b'
fraction1 = 0.3
fraction2 = 0.7
quality = 1  # Fully vapor state

# Function to calculate temperature for each state
def calculate_temperature(pressure, fluid1, fluid2, fraction1, fraction2, quality):
    try:
        # Calculate properties for each component
        T1 = CP.PropsSI('T', 'P', pressure, 'Q', quality, fluid1)
        T2 = CP.PropsSI('T', 'P', pressure, 'Q', quality, fluid2)

        # Combine temperatures based on mass fractions
        mixture_temperature = fraction1 * T1 + fraction2 * T2
        return mixture_temperature
    except Exception as e:
        return str(e)

# Calculating temperatures for states 10 to 13
temperatures = [calculate_temperature(pressure, fluid1, fluid2, fraction1, fraction2, quality) 
                for pressure in state_data]

print(temperatures)

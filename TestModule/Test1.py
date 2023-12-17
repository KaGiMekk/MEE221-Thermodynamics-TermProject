import CoolProp.CoolProp as CP

def calculate_mixture_temperature_by_pressure(fluid1, fluid2, fraction1, fraction2, given_pressure, quality):
    """
    Calculate the temperature of a binary mixture given the pressure and quality.

    :param fluid1: Name of the first fluid
    :param fluid2: Name of the second fluid
    :param fraction1: Mass fraction of the first fluid
    :param fraction2: Mass fraction of the second fluid
    :param given_pressure: Given pressure (Pa)
    :param quality: Vapor quality (fraction of vapor in the mixture)
    :return: Temperature of the mixture (K)
    """
    try:
        # Calculate properties for each component
        T1 = CP.PropsSI('T', 'P', given_pressure, 'Q', quality, fluid1)
        T2 = CP.PropsSI('T', 'P', given_pressure, 'Q', quality, fluid2)

        # Combine temperatures based on mass fractions (approximation)
        mixture_temperature = fraction1 * T1 + fraction2 * T2
        return mixture_temperature
    except ValueError as e:
        print(f"Error in calculation: {e}")
        return None

# Example usage
fluid1 = 'Isopentane'
fluid2 = 'R142b'
fraction1 = 0.3
fraction2 = 0.7
given_pressure = 1890000  # Example pressure in Pascals (1 atm)
quality = 1  # Example quality (50% vapor)

temperature = calculate_mixture_temperature_by_pressure(fluid1, fluid2, fraction1, fraction2, given_pressure, quality)
if temperature is not None:
    print(f"The approximated temperature of the mixture at given conditions is: {temperature} K")
else:
    print("Unable to calculate the temperature under given conditions.")

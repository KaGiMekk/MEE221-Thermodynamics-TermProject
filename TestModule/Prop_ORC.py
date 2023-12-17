import CoolProp.CoolProp as CP

# Input Parameters
temp = [309.46, 394.85, 342.945, 305.32]
pressure = [1890, 1890, 302.91, 302.91]
mass_fraction_isopentane = 0.3
mass_fraction_R142b = 0.7

entropy_mixture = []

# Iterate over the index
for idx in range(len(temp)):
    # Calculate properties for each component
    entropy_isopentane = CP.PropsSI('S', 'P', pressure[idx], 'T', temp[idx], 'Isopentane')
    entropy_R142b = CP.PropsSI('S', 'P', pressure[idx], 'T', temp[idx], 'R142b')

    # Calculate mixture entropy
    entropy_mix = mass_fraction_isopentane * entropy_isopentane + mass_fraction_R142b * entropy_R142b
    entropy_mixture.append(entropy_mix)

# Print entropy for each mixture in the list
for mix_entropy in entropy_mixture:
    print(f"Entropy of the Mixture: {mix_entropy} J/(kg·K)")
import numpy as np

# Temperature data
temperatures = np.array([18.5, 19, 20, 25.0, 2, 30, 13.9])

# Define function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius_array): 
    return (celsius_array * 9/5) + 32 

# Calculate average, lowest, and highest temperatures
average_temp = np.mean(temperatures)
lowest_temp = np.min(temperatures)
highest_temp = np.max(temperatures)

# Print average, lowest, and highest temperatures
print(f"Average temperature: {average_temp:.1f}°C")
print(f"Lowest temperature: {lowest_temp:.1f}°C")
print(f"Highest temperature: {highest_temp:.1f}°C\n")

# Convert and print temperatures to Fahrenheit 
fahrenheit_temps = celsius_to_fahrenheit(temperatures) 
print("Temperatures in Fahrenheit:") 
print("\n".join(f"{temp:.1f}°F" for temp in fahrenheit_temps))

# Find and print days with temperatures above 20°C
print("\nDays with temperatures above 20°C:")
above_20_temp = np.where(temperatures > 20)[0]
for index in above_20_temp: 
    print(f"Day {index + 1}: {temperatures[index]:.1f}°C")
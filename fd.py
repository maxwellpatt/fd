import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read in the data
nov3 = pd.read_csv("fanduel_nov5OrganizedF.csv")
print("Read file successfully")

# Handle missing values if necessary
nov3_clean = nov3.dropna(subset=['FPPG', 'Salary'])

# Define the degree of the polynomial
degree = 2

# Perform polynomial regression and get coefficients
coefficients = np.polyfit(nov3_clean['Salary'], nov3_clean['FPPG'], degree)

# Create the polynomial function string
equation = f'Equation: {coefficients[0]:.2e}x^2 + {coefficients[1]:.2e}x + {coefficients[2]:.2e}'

# Now you can use 'equation' in the plt.annotate call
plt.annotate(equation, xy=(0.05, 0.95), xycoords='axes fraction', fontsize=12)

# Create a polynomial function with the obtained coefficients
poly_func = np.poly1d(coefficients)

# Generate x values (salary) for plotting the polynomial function
x_values = np.linspace(nov3_clean['Salary'].min(), nov3_clean['Salary'].max(), 100)

# Generate y values (FPPG) for plotting
y_values = poly_func(x_values)

# Save the plot without the legend and with just the equation displayed

# Scatter plot of FPPG vs. Salary
plt.figure(figsize=(10, 6))
plt.scatter(nov3_clean['Salary'], nov3_clean['FPPG'], alpha=0.5)
plt.title('FPPG vs. Salary')
plt.xlabel('Salary ($)')
plt.ylabel('Fantasy Points Per Game (FPPG)')
plt.grid(True)

# Plot the polynomial regression line
plt.plot(x_values, y_values, 'r')

# Display the polynomial equation on the graph
plt.annotate(equation, xy=(0.05, 0.95), xycoords='axes fraction', fontsize=12)

# Save the figure
plt_path = "fppg_vs_salary_polynomial_fit.png"
plt.savefig(plt_path, bbox_inches='tight')

# Provide the path to the saved figure
plt_path


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read in the data
nov3 = pd.read_csv("fanduel_nov5OrganizedF.csv")
print("Read file successfully")

# Filter out players with salaries above $4000 and with relevant positions
positions_of_interest = ['PG', 'SG', 'SF', 'PF', 'C']
nov3_filtered = nov3[nov3['Salary'] > 4000]
nov3_filtered = nov3_filtered[nov3_filtered['Roster Position'].isin(positions_of_interest)]

# Group by 'Roster Position' and calculate average FPPG for the top 30 players by FPPG in each position
position_average_fppg = nov3_filtered.groupby('Roster Position').apply(
    lambda x: x.nlargest(30, 'FPPG')['FPPG'].mean()
).reset_index(name='Average FPPG')

# Calculate the average salary for each position
average_salary_by_position = nov3_filtered.groupby('Roster Position')['Salary'].mean().reset_index()

# Merge the average salary with the average FPPG to calculate 'Points Per Hundred Dollars'
value_by_position = pd.merge(average_salary_by_position, position_average_fppg, on='Roster Position')
value_by_position['Points Per Hundred Dollars'] = (value_by_position['Average FPPG'] / value_by_position['Salary']) * 100

# Sort by 'Points Per Hundred Dollars' to see which positions offer the most points for every hundred dollars spent
value_by_position_sorted = value_by_position.sort_values(by='Points Per Hundred Dollars', ascending=False)

# Print the sorted average FPPG by position
print(value_by_position_sorted)

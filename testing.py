import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

try:
    # Read in the data
    file_path = "fanduel_nov5organizedF.csv"  # Ensure this is the correct file path
    df = pd.read_csv(file_path)
    print("Read file successfully:", file_path)

    # Filter out players with salaries above $4000
    df = df[df['Salary'] > 4000]
    print("Filtered players with salary above $4000:", df.shape)

    # Define the positions of interest
    positions_of_interest = ['PG', 'SG', 'SF', 'PF', 'C']
    print("Positions of interest:", positions_of_interest)

    # Explode the 'Roster Position' column for players with multiple positions
    df['Roster Position'] = df['Roster Position'].str.split('/')
    df_exploded = df.explode('Roster Position')
    print("Exploded positions:", df_exploded['Roster Position'].unique())

    # Filter the exploded DataFrame to only include the positions of interest
    df_positions = df_exploded[df_exploded['Roster Position'].isin(positions_of_interest)]
    print("Filtered positions dataframe:", df_positions.shape)

    # Now we need to ensure we have 30 players for each position
    top_players_by_position = df_positions.groupby('Roster Position').apply(
        lambda x: x.nlargest(30, 'Salary')
    ).reset_index(drop=True)
    print("Top players by position:", top_players_by_position.groupby('Roster Position').size())

    # Calculate the average FPPG and salary for the top 30 players in each position
    position_stats = top_players_by_position.groupby('Roster Position').agg(
        Average_FPPG=('FPPG', 'mean'),
        Average_Salary=('Salary', 'mean'),
        Player_Count=('Nickname', 'count')  # Adding player count directly here
    ).reset_index()

    # Calculate 'Points Per Hundred Dollars'
    position_stats['Points Per Hundred Dollars'] = (position_stats['Average_FPPG'] / position_stats['Average_Salary']) * 100

    # Sort by 'Points Per Hundred Dollars'
    position_stats_sorted = position_stats.sort_values('Points Per Hundred Dollars', ascending=False)

    # Display the sorted table
    print("Position stats sorted:")
    print(position_stats_sorted)

    # Set the style for seaborn
    sns.set_style("whitegrid")

    # Plot the density for each position's FPPG
    plt.figure(figsize=(10, 6))
    for position in positions_of_interest:
        subset = df_positions[df_positions['Roster Position'] == position]
        sns.kdeplot(subset['FPPG'], label=position, bw_adjust=0.5)

    plt.title('Density of FPPG Across Positions')
    plt.xlabel('Fantasy Points Per Game (FPPG)')
    plt.ylabel('Density')
    plt.legend(title='Position')
    plt.show()

except Exception as e:
    print("An error occurred:", e)

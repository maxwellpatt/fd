from pulp import LpProblem, LpVariable, lpSum, LpMaximize, PULP_CBC_CMD

# Create a linear programming problem
prob = LpProblem("Maximize_FPPG", LpMaximize)

# Define decision variables
player_vars = {player: LpVariable(player, cat='Binary') for player in players}

# Define the objective function
prob += lpSum([player_vars[player] * players[player]['FPPG'] for player in players])

# Define constraints (salary cap, positional constraints)
prob += lpSum([player_vars[player] * players[player]['Salary'] for player in players]) == 66000
for position in position_counts:
    prob += lpSum([player_vars[player] for player in players if position in players[player]['Roster Position']]) == position_counts[position]

# Solve the linear programming problem
prob.solve(PULP_CBC_CMD(msg=0))

# Extract the lineup from the solved problem
lineup = {position: [] for position in position_counts}
for player in player_vars:
    if player_vars[player].value() == 1:
        for position in lineup:
            if position in players[player]['Roster Position']:
                lineup[position].append((player, players[player]['Salary'], players[player]['FPPG']))
                break

# Show the lineup and the remaining salary
lineup, prob.objective.value()

from prettytable import PrettyTable

table = PrettyTable()

# add columns: col name and values
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

# table styling: left aligned
table.align = "l"

print(table)
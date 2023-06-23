from prettytable import PrettyTable
table = PrettyTable()
table.add_column ("Pokemon Name", ["Pikachu", "Squirtle", "Charmandon", "sS"])
table.add_column ("Type", ["Koushik", "Soubhik", "Tapas Sadhu", "KS"])
table.align = "l" #left align
print(table)
table.align = "r" #Right align
print(table)
table.align = "c" #Center align
print(table)
#table.align = "none"
#print(table)
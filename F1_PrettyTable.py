from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ["Position","Driver","Number","Country","Car","Points","Gap"]

table.add_row([1,"Max Verstappen","33","Netherlands","Red Bull","208","0"])
table.add_row([2,"Charles Leclerc","16","Poland","Ferrari","170","-63"])
table.add_row([3,"Sergio Perez","11","Mexcio","Red Bull","163","-70"])
table.add_row([4,"Carlos Sainz","55","Spain","Ferrari","143","-89"])
table.add_row([5,"Geroge Russell","63","Great Britain","Mercedes","144","-90"])
table.add_row([6,"Lewis Hamilton","44","Great Britain","Mercedes","127","-106"])
table.add_row([7,"Lando Norris","4","Great Britain","McLaren","70","-163"])
table.add_row([8,"Esteban Ocon",31,"France","Alpine F1 Team",56,-177])
table.add_row([9,"Valtteri Bottas",63,"Finland","Alfa Romeo",46,-187])
table.add_row([10,"Fernando Alonso",14,"Spain","Alpine F1 Team",37,-196])
table.add_row([11,"Kevin Magnussen",20,"Dainsh","Haas F1 Team",22,-211])
table.add_row([12,"Daniel Ricciardo",3,"Australia","McLaren",19,-214])

print(table)

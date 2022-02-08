# List with adding a value
team = ["Dan", "George", "Nabil", "Joseph"]
team.append("Ryan")

print(team) 
print(team[4])

# Multi-dimentional lists
cool_cows = ["Winnie the Moo", "Moolan", "Milkshake", "Mooana"]
cool_sheep = ["Baaaart", "Baaaarnaby"]
cool_pigs = ["Chris P. Bacon", "Hamlet", "Hogwarts"]

cool_animals = [cool_cows, cool_sheep, cool_pigs]

print(cool_cows)
cool_cows.pop()
# removes last item on cool_cows list
print(cool_cows)

cool_sheep.append("Baaarbraa")
# adds "Baaarbraa" to cool_sheep list

print(cool_animals[1][2])
#Prints Baaarbraa"

# Dictionary with finding a value 
books = {"The Handmaiden's Tale":"Margaret Atwood", "The Hobbit":"J.R.R. Tolkien", "Charlie and the Chocolate Factory":"Roald Dahl"}
print(books["The Handmaiden's Tale"])



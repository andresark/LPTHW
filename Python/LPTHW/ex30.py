people = 300
cars = 40
trucks = 150


if cars > people:
    print("We should take the cars.")
elif cars < people: # ELIF is like case on C++
    print("We should not take the cars.")
else:
    print("We can't device.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")
#3-7

#program from 3-6
people_invited= ["Bil Gates", "Hideo kojyma", "Scarlette Johanson"]
people_invited.insert(0,"The Rock")
people_invited.insert(2,"Chris Evans")
people_invited.append("Emilia Clark")

for people_invite in people_invited:
    print(f"Dear {people_invite}, I would like to invite you for a dinner with me.")

for people_invite in people_invited:
    print(f"Dear,{people_invite}, i'm sorry to inform that i can only invite 2 people to our dinner.")

while len(people_invited) > 2:
    removed_people_invite = people_invited.pop()
    print(f"Sorry, {removed_people_invite}, I can't invite you to dinner.")

for people_invite in people_invited:
    print(f"Dear {people_invite}, you are still invited to dinner!")

del people_invited[:]


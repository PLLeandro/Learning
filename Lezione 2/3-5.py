#3-5

#program from 3-4

people_invited=["Bil Gates", "Hideo kojyma", "Scarlette Johanson"]

for people_invite in people_invited:
    print(f"Dear {people_invite}, I would like to invite you for a dinner with me.")

print("Bil Gates cant join us cause he is sick")

people_invited.remove("Bil Gates")
people_invited.append("Sam Remis")

for people_invite in people_invited:
    print(f"Dear {people_invite}, I would like to invite you for a dinner with me.")
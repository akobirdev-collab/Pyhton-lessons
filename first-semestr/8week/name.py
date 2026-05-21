pet_owners = ["Paul", "Andrea", "Marta"]
pets = ["Fluffy", "Bubbles", "Captain Catsworth"]
for owner, pet in zip(pet_owners, pets):
    print(f"{owner} owns {pet}.")


zip_obj = zip([1, 2], [3, 4])
print(list(zip_obj))

a = [1, 2, 3, 4]
b = [10, 20]

pairs = list(zip(a, b))
print(pairs)


data = [("Ali", (90, 85)), ("Vali", (80, 75))]

names, scores = zip(*data)

print(names)
print(scores)


print(list(zip(*[(1, 2), (3, 4), (5, 6)])))
data = [1, 2, 3, 4, 5, 6]
first, *middle, last = data
print(middle)
scores = [60, 85, 90, 70]
for i, s in enumerate(scores):
    if s > 80:
        print(i, s)

fav_foods=["dumplings", "sushi", "pasta", "pizza", "rice"]
last_purchases=[10.00, 5.00, 12.00, 20.00, 15.00]
names=["Alex", "Rachel", "Monica", "Ross", "Lisa"]

print(len(fav_foods))
for x in fav_foods:
    print(x)

print(last_purchases.reverse())

did_i_eat = "dumplings" in fav_foods
print("Did I eat?", did_i_eat)

numbers=[1,2,3,2,1]
for num in numbers:
    print(num)
print(" ")
for i in len(numbers):
    print(numbers[i])

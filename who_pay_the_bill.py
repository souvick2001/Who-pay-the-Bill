import random
print("Who paying today's bill ? 🤔")
input_name = input("Enter Everyone's names (Enter the name separated by one comma(',') and than a space) : ")
name = input_name.split(", ")
num_itmes = len(name)
names=  random.randint(0,num_itmes -1)

who_pay = name[names]
print(who_pay + " is going to buy the meal today .🫡 😁")

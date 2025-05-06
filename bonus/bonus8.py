date = input("Enter current date: ")
rate = int(input("Rate your mood today: "))
text = input("Enter your thoughts: ")

with open(f"./journal/{date}.txt", "w") as file:
    file.write(f"Mood rate: {rate}\n")
    file.write(text)
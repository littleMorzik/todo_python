import json

with open("question.json", "r") as file:
    content = file.read()
    data = json.loads(content)

correct = 0
incorrect = 0

for question in data:
    print(question["question"])
    for index, variant in enumerate(question["variants"]):
        print(f"{index + 1}. {variant}")
    answer = int(input("Choose correct answer: "))

    if answer == question["correct_answer"]:
        correct += 1
    else:
        incorrect += 1

print("You ended the test!")
print(f"Your result is\n{correct} correct answers;\n{incorrect} incorrect answers")
if correct > incorrect:
    print("You passed the test")
else:
    print("You did not pass the test")



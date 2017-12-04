import analysis

from db import db

print("Select a Problem to Analyze:")
print("\t1: Problem 1: How is a movie's budget related to its gross profit?")
print("\t2: Problem 2: Does the length of a movie affect its profitability or ratings?")
print("\t3: Problem 3: Is the director's popularity statistically correlated with the ratings or profitability of a film.")
print("\t4: Problem 4: Does content rating affect how many people will watch a movie?")
print("\t5: Problem 5: How has interest in specific genres changed for different regions? What are the most popular genres now?")
print("Type 'exit' to exit.")

i = ""

database = db()

while(i != "exit"):
    if i == 1:
        pass
    i = input("Your Choice >")
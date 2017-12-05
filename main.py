from analysis.p1 import p1
from analysis.p2 import p2
from analysis.p3 import p3
from analysis.p4 import p4
from analysis.p5 import p5

from warnings import simplefilter
simplefilter(action='ignore', category=FutureWarning)

from db import db


i = ""

database = db()#initialize a connection to the database
print("Database connection initialized.")

while(i != "exit"):#commands to analyze each of the 5 questions
    if i == str(1):
        p1(database)
    elif i == str(2):
        p2(database)
    elif i == str(3):
        p3(database)
    elif i == str(4):
        p4(database)
    elif i == str(5):
        p5(database)

    print("Select a Problem to Analyze:")
    print("\t1: Problem 1: How is a movie's budget related to its gross profit?")
    print("\t2: Problem 2: Does the length of a movie affect its profitability or ratings?")
    print(
        "\t3: Problem 3: Is the director's popularity statistically correlated with the ratings or profitability of a film.")
    print("\t4: Problem 4: Does content rating affect how many people will watch a movie?")
    print(
        "\t5: Problem 5: How has interest in specific genres changed for different regions? What are the most popular genres now?")
    print("Type 'exit' to exit.")
    i = input("Your Choice >")

database.disconnect()#close database connection connection
print("Database connection closed.")
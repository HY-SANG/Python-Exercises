"""
Python Mad Libs
In this project, we'll use Python to write a Mad Libs word game! Mad Libs have short stories with blank spaces that a player can fill in. The result is usually funny (or strange).

Mad Libs require:

A short story with blank spaces (asking for different types of words).
Words from the player to fill in those blanks.
"Roses are Red" poem example:

Mad Libs Example

For this project, we have provided the story, but it will be up to you to complete the following:

Prompt the user for inputs.
Print the story with the inputs in the right places.
Let's begin!
"""

# The template for the story

STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %ss were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %ss very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %ss ruled the world."

print "Mad Libs is starting!"

name = raw_input("Enter a name: ")
adj1 = raw_input("Enter an adjective: ")
adj2 = raw_input("Enter a second adjective: ")
adj3 = raw_input("Enter one more adjective: ")
verb = raw_input("Enter a verb: ")
noun1 = raw_input("Enter a noun: ")
noun2 = raw_input("Enter a second noun: ")
animal = raw_input("Enter an animal: ")
food = raw_input("Enter a food: ")
fruit = raw_input("Enter a fruit: ")
superhero = raw_input("Enter a superhero: ")
country = raw_input("Enter a country: ")
dessert = raw_input("Enter a dessert: ")
year = raw_input("Enter a year: ")

print STORY % (name, adj1, adj2, animal, food, verb, noun1, fruit, adj3, name, superhero, name, country, name, dessert, name, year, noun2)
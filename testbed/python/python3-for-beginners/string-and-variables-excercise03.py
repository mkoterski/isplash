# Strings and Variables - Excercise 03:
#
# Write a Python program that prompts for input and displays a cat "saying" what was provided by
# the user. Place the input provided by the user inside a speech bubble. Make the speech bubble
# expand or contract to fit around the input provided by the user.
#
# Created: 2020-09-06
# Updated: 2020-09-06
# By:      Matthias Koterski

dataentry = str(input("What does the cat say?"))
print("")
print("           |" + "-" * 10 + "|")
print("           | " + dataentry + " |")
print("           |" + "-" * 10 + "|")
print(" //////    |")
print("( o.o )  --")
print(" > ^ <")
print("")


# Output Result
# Please enter something random: Hallo wie geht es dir?
# You just entered: Hallo wie geht es dir?
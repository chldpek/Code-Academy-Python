#Section 3.1 Strings
brian = "Hello life!"

#Section 3.2
# Assign your variables below, each on its own line!
caesar = "Graham"
praline = "John"
viking = "Teresa"

# Put your variables above this line

print caesar
print praline
print viking

#Section 3.3
# The string below is broken. Fix it using the escape backslash!

'This isn\'t flying, this is falling with style!'

#Section 3.4
"""
The string "PYTHON" has six characters,
numbered 0 to 5, as shown below:

+---+---+---+---+---+---+
| P | Y | T | H | O | N |
+---+---+---+---+---+---+
  0   1   2   3   4   5

So if you wanted "Y", you could just type
"PYTHON"[1] (always start counting from 0!)
"""
fifth_letter = "MONTY"[4]

print fifth_letter

#Section 3.5 LENGTH
parrot = "Norwegian Blue"
print len(parrot)

#Section 3.6 LOWER CASE
parrot = "Norwegian Blue"

print parrot.lower()

#Section 3.7
parrot = "norwegian blue"

print parrot.upper()

#Section 3.8
pi = 3.14
print str(pi)

#Section 3.9
ministry = "The Ministry of Silly Walks"

print len(ministry)
print ministry.upper()

#Section 3.10 PRINT STRING
print "Monty Python"

#Section 3.11 PRINT VARIABLE
the_machine_goes = "Ping!"
print the_machine_goes

#Section 3.12
print "Spam " + "and " + "eggs"

#Section 3.13
print "The value of pi is around " + str(3.14)

#Section 3.14
string_1 = "Camelot"
string_2 = "place"
print "Let's not go to %s. 'Tis a silly %s." % (string_1, string_2)

#Section 3.15
name = raw_input("What is your name?")
quest = raw_input("What is your quest?")
color = raw_input("What is your favorite color?")

print "Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color)

#Section 3.16
my_string = "whatever"
print len(my_string)
print my_string.upper()

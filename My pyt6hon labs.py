import math
math.radians(32)

#printing out the surface area and volume of a sphere.

def radius():
    radius = int(input("radius"))
    area = (math.pi * radius * radius)
    volume = (2 * math.pi * radius)
    answers = {"area" : area, "volume" : volume}
    print (answers)

# splitting a sentence into its words

sentence = ("where are you" ,"ana" , "kofi")

print (sentence)


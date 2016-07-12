"""
Prints out all the melons in our inventory
"""

from melons import melons  # from melons.py file, import melons dictionary


def print_melons(melon_data):  # takes in out data that we imported
    """Prints the melon, its attributes, and values of those attributes"""

    for melon, traits in melon_data.items():  # from key, value in our file, we extract tuples and unpack into 'melon' and 'traits'. Accesses the first layer of the dictionary, which is the name of the melon.
        print melon.upper()  # uppercase our melon key because it will never change
        for traits, trait_values in traits.items():  # accessing our values from our traits after entering a level through our dictinoary (after our melon names)
            print "{}: {}".format(traits, trait_values)  # print out our traits and values of our melon
        print  # prints a new line to make it clear

print_melons(melons)

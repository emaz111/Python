"""

Binary Number Loop

This program loops through 128 denary (Base 10) numbers and converts them to 8 bit binary (Base 2)
numbers by using a loop

"""
"""
__Author__ = Emaz Khan
__Email__ = U1859269@unimail.hud.ac.uk
__Date__ = Thursday 8th November 2018
"""

for i in range(128):
    print(str(i) + " " + bin(i)[2:].zfill(8))

#!/usr/bin/python3

class Vehicle:

    # constructor
    def __init__(self, max_speed, mileage):
        # instance variables
        self.max_speed = max_speed
        self.mileage = mileage

modelX = Vehicle(240, 18)
print(modelX.max_speed, modelX.mileage)

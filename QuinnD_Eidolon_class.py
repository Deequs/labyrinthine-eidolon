#!/usr/bin/env python3
#
# Problem: Final Project
# Files:
#     None
# 
# Author: Devin Quinn
# Date: 27/04/2026
#
# provide comments for each section of code
#Imports random to allow for selection from the list
import random
#Define class
class Eidolon:
    def __init__(self, name="", loc1="", loc2="", tier=0):
        self.name = name
        self.loc1 = loc1
        self.loc2 = loc2
        self.tier = tier

    """Make a list of NHP/MONIST-entity names from existing LANCER material"""
    name_list = ["OVERLAND//KINGWATCHER", "BEGGAR_ONE", "MENDICANT_TWO", "HIEROPHANT_THREE", "WONDER_FOUR", "METAT-AUN", "RA", "DHIYED"]
    """Create the list of possible 3x3 grid locations"""
    grid_locations_list = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
    """Method to assign a random name to the object from the name list, and a tier based on the name."""
    def assign_name_and_tier(self):
        self.name = random.choice(self.name_list)
        match self.name:
            case "OVERLAND//KINGWATCHER":
                self.tier = 3
            case "BEGGAR_ONE":
                self.tier = 1
            case "MENDICANT_TWO":
                self.tier = 2
            case "HIEROPHANT_THREE":
                self.tier = 3
            case "WONDER_FOUR":
                self.tier = 3
            case "METAT-AUN":
                self.tier = 3
            case "RA":
                self.tier = 3
            case "DHIYED":
                self.tier = 2
    """Method to assign 2 locations to the object"""
    def assign_locations(self):
        """Helper method to check if the 2 locations are the same, and if so, reassign them until they are different"""
        def _check_locations(self):
            if self.loc1 == self.loc2:
                self.assign_locations()
        self.loc1 = random.choice(self.grid_locations_list)
        self.loc2 = random.choice(self.grid_locations_list)
        _check_locations(self)
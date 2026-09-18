#!/usr/bin/env python3
#
# Problem: Final Project
# Files:
#     QuinnD_Eidolon_class.py
# 
# Author: Devin Quinn
# Date: 27/04/2026
#
# provide comments for each section of code
import random
from QuinnD_Eidolon_class import Eidolon

def test_eidolon():
    """Test the Eidolon class and associated functions"""
    """Create an Eidolon and assign it a name, tier, and locations"""
    eidolon = Eidolon()
    eidolon.assign_name_and_tier()
    eidolon.assign_locations()
    """Check that the name is in the name list"""
    assert eidolon.name in Eidolon.name_list
    """Check that the tier is correct based on the name"""
    match eidolon.name:
        case "OVERLAND//KINGWATCHER":
            assert eidolon.tier == 3
        case "BEGGAR_ONE":
            assert eidolon.tier == 1
        case "MENDICANT_TWO":
            assert eidolon.tier == 2
        case "HIEROPHANT_THREE":
            assert eidolon.tier == 3
        case "WONDER_FOUR":
            assert eidolon.tier == 3
        case "METAT-AUN":
            assert eidolon.tier == 3
        case "RA":
            assert eidolon.tier == 3
        case "DHIYED":
            assert eidolon.tier == 2
    """Check that the locations are in the grid locations list and are not the same"""
    assert eidolon.loc1 in Eidolon.grid_locations_list
    assert eidolon.loc2 in Eidolon.grid_locations_list
    assert eidolon.loc1 != eidolon.loc2
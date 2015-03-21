#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Creates a List of Player Matchups in a Tournament"""


def get_matches(players):
    match_list = [item for item in players]
    for index, name in enumerate(players):
        print index, name
        
        
if __name__ == '__main__':
    print get_matches(['Harry','Howard','Hugh'])

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Creates a List of Player Matchups in a Tournament"""


def get_matches(players):
    new_list = []
    match_list = [item for item in players]
    for index, name in enumerate(players):
        for index2, name2 in enumerate(match_list, start =1):
            if index2 > index:
                new_list.append((name, name2))
    return new_list

if __name__ == '__main__':
    print get_matches(['Harry','Howard','Hugh'])

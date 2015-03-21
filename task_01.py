#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Creates a List of Player Matchups in a Tournament"""


def get_matches(players):
    new_list = []
    for index, name in enumerate(players, start = 0):
        for index2, name2 in enumerate(players, start = 1):
            if index < index2 and not index:
                new_list.append((name, name2))
            else:
                pass
    return new_list
                

if __name__ == '__main__':
    print get_matches(['Harry','Howard','Hugh'])

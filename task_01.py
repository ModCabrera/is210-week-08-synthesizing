#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Creates a List of Player Matchups in a Tournament"""


def get_matches(players):
    new_list = []
    for index, name in enumerate(players):
        for index2, name2 in enumerate(players):
            if index2 < index:
                continue
            if index is not index2:
                new_list.append((name, name2))
    return new_list

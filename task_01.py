#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Creates a List of Player Matchups in a Tournament"""


def get_matches(players):
    """Creates a list of versus matchups for players in a tournament.

    Args:
        players (list): A list of players.

    Returns:
        new_list (list): A newly created list of tuples, containing players.

    Examples:
        >>> import task_01
        >>> task_01.get_matches(['Harry', 'Howard', 'Hugh'])
        [('Harry', 'Howard'), ('Harry', 'Hugh'), ('Howard', 'Hugh')]
    """
    new_list = []
    for index, name in enumerate(players):
        for index2, name2 in enumerate(players):
            if index2 < index:
                continue
            if index is not index2:
                new_list.append((name, name2))
    return new_list

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Just some docstring"""
import authentication
import getpass


def login(username, maxattempts=3):
    """Login system to authenticate a username and password.

    Args:
        username (str): Username of user
        maxattempts (int, optional): Maximum allowed attempts to enter password.

    Returns:
        authenticated (bool): True if username,password are correct,else False.

    Examples:
        >>> task_02.login('mike', 4)
        Please enter your password:
        Incorrect username or password. You have 3 attempts left.
        Please enter your password:
        Incorrect username or password. You have 2 attempts left.
        Please enter your password:
        Incorrect username or password. You have 1 attempts left.
        Please enter your password:
        Incorrect username or password. You have 0 attempts left.
        False

        >>> task_02.login('veruca', 2)
        Please enter your password:
        Incorrect username or password. You have 1 attempts left.
        Please enter your password:
        True
    """
    authenticated = False
    user_p = 'Please enter your password:'
    err_mesg = 'Incorrect Username and Password. You have {} atempts left.'
    while maxattempts:
        print user_p
        password = getpass.getpass()
        authenticated = authentication.authenticate(username,password)
        maxattempts = maxattempts - 1
    
        if password == authenticated and maxattempts <= 3:
            return authenticated
        elif password != authenticated and maxattempts > 3:
            return False
        else:
            print err_mesg.format(maxattempts)
    return authenticated

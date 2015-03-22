#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Just some docstring"""
import authentication
import getpass


def login(username, maxattempts = 3):
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

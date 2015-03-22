#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Just some docstring"""
import authentication
import getpass


def login(username, maxattempts = 4):
    authenticated = False
    user_p = 'Please enter your password:'
    err_mesg = 'Incorrect Username and Password. You have {} atempts left.'
    while maxattempts > 0 and authenticated == False:
        print user_p
        password = getpass.getpass()
        if password != authentication.authenticate(username, password):
            maxattempts = maxattempts - 1
            print err_mesg.format(maxattempts)
        else:
            continue
    return authentication.authenticate(username,password)  

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Just some docstring"""
import authentication
import getpass

def login(username, maxattempts):
    authenticated = False
    pass_message = getpass.getpass('Please enter your password:')
    err_message = getpass.getpass('Incorrect username and password. You have {} attempts left.')
    while authenticated:
        return pass_message
        if authenticated != authentication.authenticate(username,pass_message):
            return err_message
        else:
            authenticated = authentication.authenticate(username,pass_message)
    return authenticated
    

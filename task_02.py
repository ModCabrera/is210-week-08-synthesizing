#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Just some docstring"""
import authentication
import getpass


def login(username, maxattempts = 4):
    authenticated = False
    user_p = getpass.getpass(prompt = 'Please enter your password:')
    err_mesg = 'Incorrect Username and Password. You have {} atempts left.'
    while maxattempts > 0:
        if user_p == authentication.authenticate(username, user_p):
            authenticated = authentication.authenticate(username, user_p)
        elif user_p:
            maxattempts = maxattempts - 1
            return err_mesg.format(maxattempts)
        return authenticated

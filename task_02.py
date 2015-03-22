#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Just some docstring"""
import authentication
import getpass



def login(username, maxattempts = 4):
    authenticated = False
    pw_messg = 'Please enter your password'
    error_messg = 'Incorrect Username and Password. You have {} atempts left.'
    while authenticated and maxattempts < 4:
        getpass.getpass(pw_messg,stream = sys.stdin)

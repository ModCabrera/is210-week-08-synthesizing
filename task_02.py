#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Just some docstring"""
import authentication
import getpass


def login(username, maxattempts = 4):
    authenticated = False
    user_password = getpass.getpass(prompt = 'Please enter your password:')
    error_messg = 'Incorrect Username and Password. You have {} atempts left.'
    if not user_password == authentication.authenticate(username, user_password):
        authenticated = authentication.authenticate(username, user_password)
    return authenticated

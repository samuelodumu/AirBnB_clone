#!/usr/bin/python3

import datetime

class User:
    id = 0
    def __init__(self, name):
            self.name = name
            self.id = User.id
            User.id += 1

now = datetime.datetime.now()

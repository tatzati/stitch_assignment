#!/usr/bin/env python

class Transaction:

    def __init__(self):
        self.commands = []

    def deposit(self, command, *args):
        """logs the command  and arguments to the command list"""
        self.commands.append((command, args))

    def rollback(self):
        """Supposedly rollback the action, actually just emptying the command list"""
        self.commands = []

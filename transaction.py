#!/usr/bin/env python

class Transaction:

    def __init__(self):
        self.commands = []

    def log(self, command, *args):
        """logs the command  and arguments to the command list"""
        self.commands.append((command, args))

    def rollback(self):
        """
        Call all deposited commands in reverse order
        """
        for command in reversed(self.commands):
            command[0](*command[1])

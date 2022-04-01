#!/usr/bin/env python

import sys
from operator import countOf

from transaction import Transaction
from utils import _parse_token


class Store:
    """Simple in-memory key-value store."""
    _commands = ['SET', 'GET', 'UNSET', 'NUMEQUALTO', 'END', 'BEGIN', 'ROLLBACK', 'COMMIT']

    def __init__(self):
        self.transactions = []
        self.store = {}

    def run(self, query):
        """Runs the provided query and returns the result."""
        tokens = query.split(' ')
        command, args = tokens[0], (_parse_token(token) for token in tokens[1:])

        if command in Store._commands:
            try:
                return Store.__dict__[command.lower()](self, *args)
            except TypeError:
                return "error"
        else:
            return "error"

    def set(self, key, value, should_log=True):
        """Set a [key] to the value [value]."""
        key_exists = self.key_exists(key)

        if not self.is_empty() and should_log:
            transaction = self.transactions[-1]
            if key_exists:
                transaction.log(self.set, key, self.get(key), False)
            else:
                transaction.log(self.unset, key, False)

        self.store[key] = value

    def get(self, key):
        """Print out the value."""
        return self.store.get(key, 'NULL')

    def unset(self, key, should_log=True):
        """Delete the key."""
        if self.key_exists(key):
            if not self.is_empty() and should_log:
                self.transactions[-1].log(self.set, key, self.get(key), False)

            self.store.pop(key)

    def numequalto(self, value):
        """Returns the number of keys that are associated with the given value"""
        return countOf(self.store.values(), value)

    def end(self):
        """Exit the program."""
        sys.exit()

    def begin(self):
        """Start a new transaction."""
        self.transactions.append(Transaction())

    def commit(self):
        """COMMIT: Closes all open transactional blocks."""
        if self.is_empty():
            return 'NO TRANSACTION'

        self.transactions = []

    def rollback(self):
        """Rollback all the commands from the most recent transaction block."""
        if self.is_empty():
            return 'NO TRANSACTION'

        self.transactions.pop().rollback()

    def is_empty(self):
        """Returns True if there are no transactions."""
        return len(self.transactions) == 0

    def key_exists(self, key):
        """Determine if the store has the key."""
        return key in self.store

#!/usr/bin/env python

import sys

from store import Store

"""
For the exercise I am assuming that the transactional part of the exercise is not supposed to actually work. 

I have used a dictionary as the store data structure as it is the simples solution and has a constant O(1) in most of
the commands except for the NUMEQUALTO operation, but that could be handled differently.
"""


def shell():
    """Shell infinitely reading commands until END command is given."""

    store = Store()

    while True:
        query = sys.stdin.readline().strip()
        if query is not None:
            result = store.run(query)
            if result is not None:
                print(result)


if __name__ == '__main__':
    shell()

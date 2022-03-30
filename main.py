#!/usr/bin/env python

import sys

from store import Store


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

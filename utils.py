#!/usr/bin/env python

def _parse_token(token):
    """If possible, converts the token into an int or float."""

    try:
        return int(token)
    except ValueError:
        try:
            return float(token)
        except ValueError:
            return token

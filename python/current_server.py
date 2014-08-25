#!/usr/bin/env python


def current_server():
    def get_server():
        with open('/Users/mschober/.current_server') as f:
            server = f.readlines()[0].replace('\n', '')
        return server

    return get_server()

print current_server()

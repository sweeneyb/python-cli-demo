#!/usr/bin/python3

import cmd
import sys

addresses = [
    'here@blubb.com',
    'foo@bar.com',
    'whatever@wherever.org',
]

class MyCmd(cmd.Cmd):
    def do_send(self, line):
        print(f'sending: {line}')

    def complete_send(self, text, line, start_index, end_index):
        if text:
            return [
                address for address in addresses
                if address.startswith(text)
            ]
        else:
            return addresses
    def do_pull(self, line):
        print(f'pulling: {line}')

    def complete_pull(self, text, line, start_index, end_index):
        if text:
            return [
                address for address in addresses
                if address.startswith(text)
            ]
        else:
            return addresses

    def complete_pull_subcommand_force(self, text, line, start_index, end_index):
        if text:
            return [
                answer for answer in ['yes', 'no']
                if answer.startswith(text)
            ]
        else:
            return ['yes', 'no']

    def do_pull_subcommand_force(self, line):
        print(f'subcommand force {line}')         

    def do_exit(self, line):
        sys.exit(0)


if __name__ == '__main__':
    my_cmd = MyCmd()
    if len(sys.argv) > 1 :
        my_cmd.onecmd(" ".join(sys.argv[1:]))
    else:
        my_cmd.cmdloop()

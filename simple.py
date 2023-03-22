#!/usr/bin/env python
"""A simple cmd2 application."""
import cmd2


class FirstApp(cmd2.Cmd):
    """A simple cmd2 application."""
    delattr(cmd2.Cmd, 'do_shell')
    delattr(cmd2.Cmd, 'do_edit')
    delattr(cmd2.Cmd, 'do_help')
    delattr(cmd2.Cmd, 'do_history')
    delattr(cmd2.Cmd, 'do_run_pyscript')
    delattr(cmd2.Cmd, 'do_run_script')
    delattr(cmd2.Cmd, 'do_set')
    delattr(cmd2.Cmd, 'do_shortcuts')
    def do_hello_world(self, _: cmd2.Statement):
        self.poutput('Hello World')

if __name__ == '__main__':
    import sys
    c = FirstApp()
    sys.exit(c.cmdloop())
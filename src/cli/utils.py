"""
Author: @matteobe

From: https://stackoverflow.com/questions/47972638/how-can-i-define-the-order-of-click-sub-commands-in-help
"""

import click


class CustomHelpOrder(click.Group):
    """
    Class enables to set the help priority for different commands in a click group.
    """

    def __init__(self, *args, **kwargs):
        self.help_priorities = {}
        super(CustomHelpOrder, self).__init__(*args, **kwargs)

    def list_commands(self, ctx):
        """reorder the list of commands when listing the help"""
        commands = super(CustomHelpOrder, self).list_commands(ctx)
        sorted_commands = sorted((self.help_priorities.get(command, 1), command) for command in commands)
        return [command[1] for command in sorted_commands]

    def command(self, *args, **kwargs):
        """
        Behaves the same as `click.Group.command()` except that it captures a priority for listing command names in
        help.
        """

        help_priority = kwargs.pop('help_priority', 1)
        help_priorities = self.help_priorities

        def decorator(f):
            cmd = super(CustomHelpOrder, self).command(*args, **kwargs)(f)
            help_priorities[cmd.name] = help_priority
            return cmd

        return decorator

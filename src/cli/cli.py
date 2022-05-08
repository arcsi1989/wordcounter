"""
Author: @arcsi1989
"""

import click

from src.cli.utils import CustomHelpOrder


@click.group(cls=CustomHelpOrder, name="src")  # TODO change src
@click.help_option("-h", "--help")
def src_cli():
    pass

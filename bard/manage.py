# coding: utf-8
import json
import click
import logging
from pprint import pprint  # noqa
from flask.cli import FlaskGroup

from bard.app import create_app


log = logging.getLogger("bard")


@click.group(cls=FlaskGroup, create_app=create_app)
def cli():
    """Server-side command line for bard."""

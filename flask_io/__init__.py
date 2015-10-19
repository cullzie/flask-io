# Make marshmallow's functions and classes importable from flask-io
from marshmallow import post_load, post_dump, Schema, ValidationError
from marshmallow.utils import missing

from .io import FlaskIO
from .errors import Error

__version__ = '1.6.0'
__author__ = 'Vinicius Chiele'
__license__ = 'MIT'

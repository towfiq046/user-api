"""Schemas"""

from flask import Flask
from marshmallow import Schema, fields
from marshmallow.validate import Range, Length


app = Flask(__name__)


class ParentSchema(Schema):
    """Parent schema"""
    id = fields.Integer(dump_only=True)
    first_name = fields.String(required=True, validate=Length(min=3, max=100))
    last_name = fields.String(required=True, validate=Length(min=3, max=100))
    street = fields.String(required=True, validate=Length(min=3, max=100))
    city = fields.String(required=True, validate=Length(min=3, max=100))
    state = fields.String(required=True, validate=Length(min=2, max=100))
    zip_code = fields.Integer(required=True, strict=True, validate=Range(min=2))


parent_schema = ParentSchema()
parents_schema = ParentSchema(many=True)


class ChildSchema(Schema):
    """Child schema"""
    id = fields.Integer(dump_only=True)
    first_name = fields.String(required=True, validate=Length(min=3, max=100))
    last_name = fields.String(required=True, validate=Length(min=3, max=100))


child_schema = ChildSchema()
children_schema = ChildSchema(many=True)

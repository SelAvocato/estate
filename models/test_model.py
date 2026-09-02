from odoo import fields, models


class TestModel(models.Model):
    _name = "test.model"
    _description = "test model of real estate"

    name = fields.Char()

from odoo import fields, models


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "type of estate property"

    name = fields.Char("Type", required=True)

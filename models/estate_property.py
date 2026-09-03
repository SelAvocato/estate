from odoo import fields, models


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "test property of real estate"

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date("Available Date")
    expected_price = fields.Float()
    selling_price = fields.Float(required=True)
    bedrooms = fields.Integer()
    living_area = fields.Integer("Living Area (sqm)")
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer("Garden Size (sqm)")
    garden_orientation = fields.Selection(
        selection=[
            ("north", "North"),
            ("south", "South"),
            ("east", "East"),
            ("west", "West"),
        ]
    )

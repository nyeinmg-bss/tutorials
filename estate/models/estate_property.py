from odoo import models,fields

class EstateProperty(models.Model):
    _name = "estate_property"
    _description = "Real Estate Property"

    name = fields.Char("name", required=True)
    description = fields.Text("description")
    postcode = fields.Char("postcode")
    date_availability = fields.Date("date_availability")
    expected_price = fields.Float("expected_price", required=True)
    selling_price = fields.Float("selling_price")
    bedrooms = fields.Integer("bedrooms")
    living_area = fields.Integer("living_area")
    facades = fields.Integer("facades")
    garage = fields.Boolean("garage") 
    garden = fields.Boolean("garden")
    garden_orientation = fields.Selection([("north", "North"), ("south", "South"), ("east", "East"), ("west", "West")])

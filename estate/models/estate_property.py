from odoo import models,fields


class EstateProperty(models.Model):
    _name = "estate_property"
    _description = "Real Estate Property"

    name = fields.Char("name", required=True)
    active = fields.Boolean("active", default=False)
    description = fields.Text("description")
    postcode = fields.Char("postcode")
    date_availability = fields.Date("date_availability", copy=False, default=fields.Date.add(fields.Date.today(), month=3))
    expected_price = fields.Float("expected_price", required=True)
    selling_price = fields.Float("selling_price", readonly=True, copy=False)
    bedrooms = fields.Integer("bedrooms", default=2)
    living_area = fields.Integer("living_area")
    facades = fields.Integer("facades")
    garage = fields.Boolean("garage") 
    garden = fields.Boolean("garden")
    garden_orientation = fields.Selection([("north", "North"), ("south", "South"), ("east", "East"), ("west", "West")])
    state = fields.Selection([("new", "New"), ("received", "Offer Received"), ("accepted", "Offer Accepted"), ("sold", "Sold"), ("cancelled", "Cancelled")], default="new", copy=False)

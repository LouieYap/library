from odoo import models, fields

class LibraryBookCategory(models.Model):
    _name = "library.book.category"
    _description = "Book Category"
    _sql_constraints = [('unique_name', 'UNIQUE(name)', 'Name must be unique!')]

    name = fields.Char(
        string="Category Name",
        required=True
    )

    
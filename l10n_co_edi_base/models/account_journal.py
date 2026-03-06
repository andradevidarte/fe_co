from odoo import fields, models


class AccountJournal(models.Model):
    _inherit = "account.journal"

    dian_document_type = fields.Selection(
        [
            ("fv", "Factura de Venta"),
            ("nc", "Nota Crédito"),
            ("nd", "Nota Débito"),
            ("export", "Factura de Exportación"),
            ("ds", "Documento Soporte"),
        ],
        string="DIAN Document Type",
    )

    dian_resolution_number = fields.Char(string="DIAN Resolution Number")
    dian_resolution_date_from = fields.Date(string="Resolution Valid From")
    dian_resolution_date_to = fields.Date(string="Resolution Valid To")
    dian_prefix = fields.Char(string="DIAN Prefix")
    dian_range_from = fields.Integer(string="Range From")
    dian_range_to = fields.Integer(string="Range To")

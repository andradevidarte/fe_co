from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    dian_is_not_obliged_to_invoice = fields.Boolean(
        string="Not obliged to invoice (Document Support)",
        help="If enabled, vendor bills for this partner can generate Documento Soporte.",
        default=False,
    )

    dian_identification_type = fields.Char(
        string="DIAN Identification Type (code)",
        help="Placeholder. Map to official DIAN catalogs in later iterations.",
    )

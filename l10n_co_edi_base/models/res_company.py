from odoo import api, fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    dian_edi_enabled = fields.Boolean(string="DIAN EDI Enabled", default=False)

    dian_environment = fields.Selection(
        [
            ("habilitacion", "Habilitación (Pruebas)"),
            ("produccion", "Producción"),
        ],
        string="DIAN Environment",
        default="habilitacion",
        required=True,
    )

    dian_test_set_id = fields.Char(string="DIAN TestSetId (Habilitación)")

    dian_cert_pfx = fields.Binary(string="DIAN Certificate (PFX/P12)", attachment=True)
    dian_cert_pfx_filename = fields.Char(string="Certificate Filename")
    dian_cert_password = fields.Char(string="Certificate Password")

    dian_contingency_enabled = fields.Boolean(
        string="Enable Contingency Mode (manual)", default=False
    )

    @api.constrains("dian_environment", "dian_edi_enabled")
    def _check_dian_environment(self):
        for company in self:
            if not company.dian_edi_enabled:
                continue

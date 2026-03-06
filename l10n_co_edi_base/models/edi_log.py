from odoo import fields, models


class L10nCoEdiLog(models.Model):
    _name = "l10n_co_edi.log"
    _description = "Colombia EDI Technical Log"
    _order = "create_date desc"

    company_id = fields.Many2one("res.company", required=True, index=True)
    move_id = fields.Many2one("account.move", index=True)

    level = fields.Selection(
        [("info", "Info"), ("warning", "Warning"), ("error", "Error")],
        default="info",
        required=True,
    )
    message = fields.Char(required=True)
    payload = fields.Text(help="Technical details (avoid secrets).")

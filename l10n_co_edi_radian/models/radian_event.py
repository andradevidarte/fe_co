from odoo import fields, models


class L10nCoRadianEvent(models.Model):
    _name = "l10n_co_radian.event"
    _description = "RADIAN Event"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "create_date desc"

    company_id = fields.Many2one("res.company", required=True, index=True)
    move_id = fields.Many2one("account.move", index=True)

    event_type = fields.Selection(
        [
            ("acuse", "Acuse de Recibo"),
            ("recibo", "Recibo del Bien/Servicio"),
            ("aceptacion", "Aceptación Expresa"),
            ("rechazo", "Rechazo"),
        ],
        required=True,
        index=True,
    )

    state = fields.Selection(
        [("draft", "Draft"), ("sent", "Sent"), ("accepted", "Accepted"), ("rejected", "Rejected")],
        default="draft",
        tracking=True,
    )

    related_uuid = fields.Char(string="Related DIAN UUID/CUFE", index=True)
    xml_attachment_id = fields.Many2one("ir.attachment", string="Event XML", copy=False)
    response_attachment_id = fields.Many2one("ir.attachment", string="DIAN Response", copy=False)

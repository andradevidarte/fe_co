from odoo import api, fields, models, _
from odoo.exceptions import UserError


class AccountMove(models.Model):
    _inherit = "account.move"

    dian_edi_state = fields.Selection(
        [
            ("disabled", "Disabled"),
            ("draft", "Draft"),
            ("queued", "Queued"),
            ("sent", "Sent"),
            ("accepted", "Accepted"),
            ("rejected", "Rejected"),
            ("contingency", "Contingency"),
        ],
        string="DIAN EDI State",
        default="disabled",
        copy=False,
        tracking=True,
    )

    dian_cufe = fields.Char(string="CUFE/CUDE", copy=False, tracking=True)
    dian_uuid = fields.Char(string="DIAN UUID", copy=False, tracking=True)

    dian_xml_attachment_id = fields.Many2one(
        "ir.attachment", string="DIAN XML", copy=False
    )
    dian_application_response_attachment_id = fields.Many2one(
        "ir.attachment", string="DIAN ApplicationResponse", copy=False
    )

    dian_error_message = fields.Text(string="DIAN Last Error", copy=False)
    dian_last_attempt_at = fields.Datetime(string="DIAN Last Attempt", copy=False)
    dian_attempt_count = fields.Integer(string="Attempt Count", default=0, copy=False)

    dian_is_document_support = fields.Boolean(
        string="Is Documento Soporte",
        compute="_compute_dian_is_document_support",
        store=True,
    )

    @api.depends("move_type", "partner_id.dian_is_not_obliged_to_invoice")
    def _compute_dian_is_document_support(self):
        for move in self:
            move.dian_is_document_support = bool(
                move.move_type in ("in_invoice", "in_refund")
                and move.partner_id.dian_is_not_obliged_to_invoice
            )

    def action_dian_queue_send(self):
        self.ensure_one()
        if not self.company_id.dian_edi_enabled:
            raise UserError(_("DIAN EDI is not enabled for this company."))

        if self.state != "posted":
            raise UserError(_("The move must be posted before sending to DIAN."))

        self.env["l10n_co_edi.queue"].create(
            {
                "company_id": self.company_id.id,
                "move_id": self.id,
                "job_type": "send_move",
            }
        )
        self.dian_edi_state = "queued"

    def action_dian_enable_contingency(self):
        self.ensure_one()
        if not self.company_id.dian_edi_enabled:
            raise UserError(_("DIAN EDI is not enabled for this company."))
        self.company_id.dian_contingency_enabled = True

    def action_dian_disable_contingency(self):
        self.ensure_one()
        self.company_id.dian_contingency_enabled = False

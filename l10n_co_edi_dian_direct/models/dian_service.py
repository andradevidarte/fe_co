from odoo import fields, models


class L10nCoDianService(models.AbstractModel):
    _name = "l10n_co_edi.dian_service"
    _description = "DIAN Direct Service (stub)"

    def send_move(self, move):
        return {
            "sent_at": fields.Datetime.now(),
            "accepted": True,
            "uuid": "TODO-UUID",
            "cufe": "TODO-CUFE",
        }

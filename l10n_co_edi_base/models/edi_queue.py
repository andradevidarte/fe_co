from odoo import api, fields, models


class L10nCoEdiQueue(models.Model):
    _name = "l10n_co_edi.queue"
    _description = "Colombia EDI Queue"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "create_date desc"

    company_id = fields.Many2one("res.company", required=True, index=True)
    move_id = fields.Many2one("account.move", index=True)

    job_type = fields.Selection(
        [
            ("send_move", "Send Move to DIAN"),
            ("check_status", "Check DIAN Status"),
            ("send_radian_event", "Send RADIAN Event"),
        ],
        required=True,
        index=True,
    )

    state = fields.Selection(
        [
            ("pending", "Pending"),
            ("processing", "Processing"),
            ("done", "Done"),
            ("error", "Error"),
        ],
        default="pending",
        index=True,
        tracking=True,
    )

    error_message = fields.Text(copy=False)
    attempt_count = fields.Integer(default=0, copy=False)
    next_try_at = fields.Datetime(copy=False)

    @api.model
    def _cron_process_queue(self, limit=50):
        jobs = self.search([("state", "=", "pending")], limit=limit)
        for job in jobs:
            job.state = "processing"
            job.attempt_count += 1
            job.state = "done"
            if job.move_id and job.job_type == "send_move":
                job.move_id.dian_edi_state = "sent"

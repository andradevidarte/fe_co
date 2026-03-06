from odoo import models


class L10nCoUblBuilder(models.AbstractModel):
    _name = "l10n_co_edi.ubl_builder"
    _description = "UBL 2.1 Builder (stub)"

    def build_move_ubl_xml(self, move):
        xml = b"<Invoice><!-- TODO: UBL 2.1 Colombia --></Invoice>"
        return xml, "dian_invoice.xml"

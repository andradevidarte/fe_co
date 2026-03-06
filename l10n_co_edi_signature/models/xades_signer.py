from odoo import models


class L10nCoXadesSigner(models.AbstractModel):
    _name = "l10n_co_edi.xades_signer"
    _description = "XAdES Signer (stub)"

    def sign_xml(self, company, xml_bytes):
        return xml_bytes

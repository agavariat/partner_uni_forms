# Copyright 2015 Antiun Ingeniería, S.L.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    x_pvereda = fields.Char(
        string="Vereda",
        help="Escriba la vereda en la que se encuentra",
    )

    

    #def _onchange_partner_id_values(self, partner_id):
        #"""Recover VAT from partner if available."""
       # result = super(Lead, self)._onchange_partner_id_values(partner_id)
        #if not partner_id:
        #    return result
        #partner = self.env["res.partner"].browse(partner_id)
        #if partner.x_vereda:
        #    result["vat"] = partner.vat
        #return result

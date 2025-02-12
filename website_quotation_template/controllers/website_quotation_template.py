# -*- coding: utf-8 -*-
###############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2024-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: Athira PS (odoo@cybrosys.com)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
from odoo import http
from odoo.http import request


class TemplateSnippet(http.Controller):
    """Adding website quotation template snippet"""

    @http.route('/quotation_template', methods=['POST'], type="json",
                auth="public", website=True)
    def website_quotation_template(self, **post):
        """Return details of products inside the quotation template."""
        templates = [
            {
                'name': temp.name,
                'id': temp.id,
                'is_available_in_website': temp.is_available_in_website,
                'image': '/web/image?model=sale.order.template&id=' + str(
                    temp.id) + '&field=temp_img'
            }
            for temp in request.env['sale.order.template'].sudo().search([])
        ]
        return templates

    @http.route('/product/details/<int:product_id>', type='http',
                auth="public", website=True)
    def product_details(self, product_id, **kwargs):
        """Render the product details template for a specific sale order
         template."""
        template = request.env['sale.order.template'].sudo().browse(product_id)
        return http.request.render(
            'website_quotation_template.product_details_template',
            {'template': template})

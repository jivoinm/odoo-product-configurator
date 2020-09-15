from openerp import models


class Website(models.Model):
    _inherit = "website"

    def sale_product_domain(self):
        """ Shows/Hides configurable products
        depending on the active marker of the
        layout_config_products_show view introduced by module"""
        domain = super(Website, self).sale_product_domain()
        ext_id = "website_product_configurator.layout_config_products_show"
        if not self.env.ref(ext_id).active:
            domain.append(("config_ok", "=", False))
        return domain

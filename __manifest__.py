# -*- coding: utf-8 -*-
{
    "name": "E-commerce Base",

    "summary": "Base for ecommerce api integration",

    "category": "Sales",

    "version": "12.0.1.0.0",

    "author": "INKERP",

    "website": "http://www.inkerp.com",

    "depends": ["sale_management", "stock"],

    "data": ["views/eg_ecom_instance_view.xml",
             "views/eg_product_template_view.xml",
             "views/eg_product_product_view.xml",
             "views/eg_product_category_view.xml",
             "views/eg_product_attribute_view.xml",
             "views/eg_attribute_value_view.xml",
             "wizards/import_from_ecom_provider_view.xml",
             "views/eg_res_partner_view.xml",
             "views/eg_template_image_view.xml",
             "views/eg_inventory_location_view.xml",
             "views/eg_sale_order_view.xml",
             "views/eg_product_attribute_line_view.xml",
             "views/eg_sync_history_view.xml",
             "views/eg_account_journal_view.xml",
             "views/eg_product_pricelist_view.xml",
             "views/account_invoice_view.xml",
             "data/test_connection_cron.xml",
             "data/eg_history_cron.xml",
             "views/sale_order_view.xml",
             "data/create_sequence.xml",
             "security/ir.model.access.csv"],
    'license': "OPL-1",
    'installable': True,
    'application': True,
    'auto_install': False,
    'pre_init_hook': 'pre_init_hook',
    'uninstall_hook': "uninstall_hook",

}

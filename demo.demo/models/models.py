# -*- coding: utf-8 -*-

from odoo import models, fields, api


class DemoDemo(models.Model):
    _name = 'demo.demo'
    _description = 'Demo Object'

    name = fields.Char(string='Name')

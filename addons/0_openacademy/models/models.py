from odoo import models, fields, api

class Course(models.Model):
    _name = 'openacademy.course' # tên bảng trong sql: openacademy_course

    name = fields.Char(string="Title", required=True)
    description = fields.Text()
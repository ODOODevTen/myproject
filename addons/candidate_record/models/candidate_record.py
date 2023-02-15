from odoo import _, api, fields, models

class CandidateRecord(models.Model):
    _name = 'candidate.record'
    _description = 'Candidate Record'
    
    name = fields.Char(string='Name', required=True)
    address = fields.Text(string='Address')
    age = fields.Integer(string='Age')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')],default='other',string='Gender')
    education = fields.Text(string='Education')
    skill = fields.Text(string='Skill')
    full_time = fields.Boolean(string='Full Time',default=False)
    marital_status = fields.Selection([
        ('married','Married'),
        ('single','Single')],default='single',string='Marital Status')

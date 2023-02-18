from odoo import _,fields, models,api
from datetime import datetime
class ImprovementSuggestion(models.Model):
    _name = 'improvement.suggestion'
    _description = 'Improvement Suggestion'
    _rec_name = 'doc_no'
    
    issue_date = fields.Date(string='Issue Date',default=datetime.today())
    employee_id = fields.Many2one('hr.employee', string ='Proposed By')
    employee_email = fields.Char(string='Proposed By Email', related='employee_id.work_email')
    designation = fields.Char(string='Designation')
    bu_br_id = fields.Char(string='Division/BU/Branch Name')
    department_id = fields.Char(string='Department Name')
    doc_no = fields.Char(string='Doc No', default='New')

    facilitator_id = fields.Many2one('hr.employee', string='Facilitated By')
    facilitator_email = fields.Char(string='Facilitated By Email',related='facilitator_id.work_email')

    dep_head_id = fields.Many2one('hr.employee', string='Department Head Name')
    dep_head_email = fields.Char(string='Department Head Email',related='dep_head_id.work_email')

    improvement_them = fields.Text(string='IMPROVEMENT THEME')
    current_condition = fields.Text(string='CURRENT CONDITION ANALYZE')
    improvement_suggestion = fields.Text(string='IMPROVEMENT SUGGESTION')

    safety_healthy = fields.Boolean(string='Safety/Healthy')
    quallity = fields.Boolean(string='Quality (next process/coutomer satisfaction)')
    cost_budget = fields.Boolean(string='Cost/Budget')
    delivery = fields.Boolean(string='Delivery (next process/ customer send on time)')
    morality = fields.Boolean(string='Morality/Good Habit')

    man_people = fields.Boolean(string='Man/People')
    machine_equipment = fields.Boolean(string='Machine/Equipment/Tools')
    method_process = fields.Boolean(string='Method/Process(SOP)')
    material_parts = fields.Boolean(string='Material/Parts')
    environment = fields.Boolean(string='Environment')
    information = fields.Boolean(string='Information')

    sort = fields.Boolean(string='Sort (Separating needed & unneeded)')
    set_in = fields.Boolean(string='Set in Order (Keep well & easy to retrieval)')
    shine = fields.Boolean(string='Shine (Neat & Clean)')
    standardize = fields.Boolean(string='Standardize (Standard for 3S above)')
    sustain = fields.Boolean(string='Sustain (Do it & maintain with discipline)')

    improvement_scope = fields.Selection([
        ('individual','Individual Improvement'),
        ('department', 'Department Improvement'),
        ('the_whole','The Whole UMG Improvement'),
        ('other','Other Improvement')
    ],default='individual', string='IMPROVEMENT SCOPE')

    before_improvement = fields.Image(string='Before Improvement')
    after_improvement = fields.Image(string='After Improvement')

    deliverables = fields.Text(string='DELIVERABLES')
    next_improvement_plan = fields.Text(string='NEXT IMPROVEMENT PLAN')

    create_id = fields.Many2one('res.users', string='Create By', default=lambda self:self.env.user)
    create_date = fields.Datetime('Create Date', default=lambda self: fields.datetime.now())

    state = fields.Selection([
        ('draft','Draft'),
        ('add','Added'),
        ('approve', 'Approved'),
        ('close','Closed'),
        ('reject','Rejected')
    ],default='draft', string='State')

    def action_add(self):
        self.state = 'add'

    def action_approve(self):
        self.state = 'close'

    def action_reject(self):
        self.state = 'reject'

    @api.model
    def create(self,vals):
        if vals.get('doc_no','New') == 'New':
            vals['doc_no'] = self.env['ir.sequence'].next_by_code('improvement.suggestion') or 'New'
        result = super(ImprovementSuggestion,self).create(vals)
        return result



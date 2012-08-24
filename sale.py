#This file is part sale_waiting module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.

from trytond.model import Workflow, ModelView, ModelSQL, fields
from trytond.pyson import Eval
from trytond.transaction import Transaction
from trytond.pool import Pool

class Sale(Workflow, ModelSQL, ModelView):
    _name = 'sale.sale'

    state = fields.Selection([
        ('draft', 'Draft'),
        ('quotation', 'Quotation'),
        ('confirmed', 'Confirmed'),
        ('processing', 'Processing'),
        ('done', 'Done'),
        ('cancel', 'Canceled'),
        ('waiting', 'Waiting'),
    ], 'State', readonly=True, required=True)

    def __init__(self):
        super(Sale, self).__init__()
        self._transitions |= set((
                ('draft', 'quotation'),
                ('quotation', 'confirmed'),
                ('confirmed', 'processing'),
                ('processing', 'processing'),
                ('draft', 'cancel'),
                ('quotation', 'cancel'),
                ('quotation', 'draft'),
                ('draft', 'waiting'),
                ('waiting', 'draft'),
                ('waiting', 'quotation'),
                ))
        self._buttons.update({
                'draft': {
                    'invisible': ~Eval('state').in_(['quotation', 'waiting']),
                    },
                'set_waiting': {
                    'invisible': Eval('state') != 'waiting',
                    },
                })

    @ModelView.button
    @Workflow.transition('waiting')
    def waiting(self, ids):
        self.set_sale_date(ids)
        pass

    @ModelView.button
    def set_waiting(self, ids):
        quotes = []
        for sale in self.browse(ids):
            if sale.state == 'waiting':
                quotes.append(sale.id)
        self.write(quotes, {
                'state': 'quotation',
                })

Sale()

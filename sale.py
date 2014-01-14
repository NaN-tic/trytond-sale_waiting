#This file is part sale_waiting module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.

from trytond.model import Workflow, ModelView, fields
from trytond.pyson import If, Eval
from trytond.pool import PoolMeta

__all__ = ['Sale']
__metaclass__ = PoolMeta

class Sale:
    'Sale'
    __name__ = 'sale.sale'
    sale_date = fields.Date('Sale Date',
        states={
            'readonly': ~Eval('state').in_(['draft', 'quotation']),
            'required': ~Eval('state').in_(['draft', 'quotation', 'cancel','waiting']),
            },
        depends=['state'])

    @classmethod
    def __setup__(cls):
        super(Sale, cls).__setup__()
        selection = ('waiting', 'Waiting')
        if selection not in cls.state.selection:
            cls.state.selection.append(selection)
        cls._transitions |= set((
                ('draft', 'waiting'),
                ('waiting', 'draft'),
                ('waiting', 'quotation'),
                ))
        cls._buttons.update({
                'draft': {
                    'invisible': ~Eval('state').in_(['cancel', 'quotation', 'waiting']),
                    'icon': If(Eval('state') == 'cancel', 'tryton-clear',
                        'tryton-go-previous'),
                    },
                'to_quotation': {
                    'invisible': Eval('state') != 'waiting',
                    },
                })

    @classmethod
    @Workflow.transition('waiting')
    def waiting(cls, sales):
        pass

    @classmethod
    @ModelView.button
    @Workflow.transition('quotation')
    def to_quotation(cls, sales):
        pass

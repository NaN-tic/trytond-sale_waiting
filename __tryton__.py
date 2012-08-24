#This file is part sale_waiting module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.
{
    'name': 'Sale Waiting',
    'name_ca_ES': 'Estat en espera a les vendes',
    'name_es_ES': 'Estado en espera a las ventas',
    'version': '2.4.0',
    'author': 'Zikzakmedia',
    'email': 'zikzak@zikzakmedia.com',
    'website': 'http://www.zikzakmedia.com/',
    'description': '''Add new option state in sale.sale: waiting.
It also modifies the workflow of sale by adding a new step state.
''',
    'description_ca_ES': '''Afegeix una nova opció a comandes: waiting.
Modifica el fluxe de les comandes afegint un nou pas en espera a la venta.
''',
    'description_es_ES': '''Añade una nueva opción a pedidos: waiting.
Modifica el flujo de los pedidos añadiendo una nueva opción en espera a la venta.
''',
    'depends': [
        'ir',
        'res',
        'sale',
    ],
    'xml': [
        'sale.xml',
    ],
    'translation': [
        'locale/ca_ES.po',
        'locale/es_ES.po',
    ]
}

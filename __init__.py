#!/usr/bin/env python
# This file is part sale_waiting module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from .sale import *


def register():
    Pool.register(
        Sale,
        module='sale_waiting', type_='model')

#!/usr/bin/env python
# This file is part of sale_waiting module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import test_depends, test_view


class SaleWaitingTestCase(unittest.TestCase):
    'Test Sale Waiting module'

    def setUp(self):
        trytond.tests.test_tryton.install_module('sale_waiting')

    def test0005views(self):
        'Test views'
        test_view('sale_waiting')

    def test0006depends(self):
        'Test depends'
        test_depends()


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        SaleWaitingTestCase))
    return suite

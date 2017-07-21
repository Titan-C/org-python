#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2017 jianglin
# File Name: test.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2017-03-16 16:28:32 (CST)
# Last Update:星期五 2017-7-21 9:20:24 (CST)
#          By:
# Description:
# **************************************************************************
import unittest
# from org1 import org_to_html
from orgpython import org_to_html
from orgpython import Org


class TestOrg(unittest.TestCase):
    def test_heading(self):
        org = Org('* heading1\n** heading2', toc=True)
        self.assertEqual(
            str(org), 'Org(Heading(* heading1),Heading(** heading2))')

    def test_bold(self):
        text = '''
        *bold* bold*
        bold* bold*
        *bold* *bold*
        '''
        html = org_to_html(text)
        self.assertEqual(html,
                         '<b>bold</b> bold*bold* bold*<b>bold</b> <b>bold</b>')

    def test_italic(self):
        text = '''
        **italic** italic*
        italic* italic*
        **italic** **italic**
        '''
        html = org_to_html(text)
        self.assertEqual(
            html,
            '<i>italic</i> italic*italic* italic*<i>italic</i> <i>italic</i>')


if __name__ == '__main__':
    unittest.main()

# -*- coding: utf-8 -*-

###################################################################################
# 
#    Copyright (C) 2017 MuK IT GmbH
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###################################################################################

import os
import base64
import logging
import unittest

from odoo import _
from odoo.tests import common

_path = os.path.dirname(os.path.dirname(__file__))
_logger = logging.getLogger(__name__)

class DMSTestCase(common.TransactionCase):
    
    at_install = True
    post_install = False
    
    def setUp(self):
        super(DMSTestCase, self).setUp()
        self.demouser = self.browse_ref("base.user_demo")
        self.dmsuser = self.browse_ref("muk_dms.user_dmsuser_demo")
        self.dmsmanager = self.browse_ref("muk_dms.user_dmsmanager_demo")
        
    def tearDown(self):
        super(DMSTestCase, self).tearDown()
        
    def file_base64(self):
        return base64.b64encode(b"Hello World!")
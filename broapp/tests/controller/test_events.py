#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
             _   ____  _____   ____   
            | | |  _ \|  __ \ / __ \  
   __ _  ___| |_| |_) | |__) | |  | | 
  / _` |/ _ \ __|  _ <|  _  /| |  | | 
 | (_| |  __/ |_| |_) | | \ \| |__| | 
  \__, |\___|\__|____/|_|  \_\\____(_)
   __/ |                              
  |___/                                


'''


from .. import BaseTestCase

class EventsTestCase(BaseTestCase):

	def test_index(self):
		test = self.getSecured("/events")
		print test
		assert True
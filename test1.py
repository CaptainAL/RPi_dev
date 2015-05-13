# -*- coding: utf-8 -*-
"""
Created on Wed May 13 06:58:19 2015

@author: Alex
"""

## Test for the Raspberry Pi    

# print current time
import datetime as dt
start_time = dt.datetime.now()
print 'Start time: '+start_time.strftime('%H:%M:%S')
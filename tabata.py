# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 17:21:12 2019

@author: dakar
"""

import time

def prep_time(prep):
    for j in list(range(prep,0,-1)):
        print('{:*^10}'.format(j))
        time.sleep(1)
        
def work_time(work,prep):
    time.sleep(work-prep)
    print('\a')
    print('Rest in:')
    prep_time(prep)

    
def rest_time(rest,prep):
    if rest>=prep:
        print('{:*^14}'.format('REST'))
        time.sleep(rest-prep)



def tabata(work,rest,num_rounds = 10,prep = 5):
    for i in range(num_rounds):
        print('\a')
        print('Beginning round {} in:'.format(i+1))
        prep_time(prep)
        print('{:*^14}'.format('WORK'))
        work_time(work,prep)
        rest_time(rest,prep)
        
    print('{:*^14}'.format('FINISHED'))
    
        

if __name__ == '__main__':
    tabata(work=60,rest=0,num_rounds=10,prep=5)
        
        
    
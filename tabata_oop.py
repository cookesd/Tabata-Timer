# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 18:21:45 2019


reference: https://pythonprogramming.net/object-oriented-programming-crash-course-tkinter/
@author: dakar
"""

import tkinter as tk

LARGE_FONT = ('Arial',12)

class TabataApp(tk.Tk):
    
    def __init__(self,*args,**kwargs):
        '''Sets up frame for tabata pages
        Inherits from tk.Tk'''
        tk.Tk.__init__(self,*args,**kwargs) #runs the Tk __init__
        
        container = tk.Frame(self) #initializes from for pages to go in
        container.pack(side='top',fill='both',expand=True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)
        
        self.frames = {}
#        frame = TimerPage(container,self)
#        self.frames[TimerPage] = frame
#        frame.grid(row=10,column=10)
#        
#        frame2 = InputPage(container,self)
#        self.frames[InputPage] = frame2
#        frame2.grid(row=0,column=0)
        
        for i,F in enumerate([InputPage, TimerPage]):
            frame = F(container,self)
            self.frames[F] = frame
            frame.grid(row=3*0,column=3*i,sticky='nsew')
        
        self.show_frame(TimerPage)
        
    def show_frame(self,controller,**kwargs):
        '''Makes the passed frame come to the top'''
        frame = self.frames[controller]
        print(controller)
#        frame.update(controller,kwargs)
        frame.tkraise() #brings this frame to the top
        
#class StartPage(tk.Frame):
#    
#    def __init__(self,parent,controller):
#        tk.Frame.__init__(self,parent)
#        label = tk.Label(self,text='Start Page',font = LARGE_FONT)
#        label.pack()
##        label.grid(row=0,column=0)
#    def update(*args,**kwargs):
#        None

class TimerPage(tk.Frame):
    
    def __init__(self,parent,controller,**kwargs):
        tk.Frame.__init__(self,parent)
        label = tk.Label(parent,text='This is the Timer Page')
        label.grid(column=0,row=0)
        
        btn = tk.Button(parent,text = 'Go to Input Page',
                        command = lambda: controller.show_frame(InputPage))
        btn.grid(column=0,row=1)
    def update(self,parent,**kwargs):
        '''Want to update what's showing with the input'''
#        print(kwargs)
#        print(type(kwargs))
#        print(kwargs.keys())
#        self.label.configure(text=kwargs['text'])
        None

      
class InputPage(tk.Frame):
    
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        work_lbl = tk.Label(parent,text='Enter work interval (seconds):')
        rest_lbl = tk.Label(parent,text='Enter rest interval (seconds):')
        prep_lbl = tk.Label(parent,text='Enter prep interval (seconds):')
        iterations_lbl = tk.Label(parent,text='Enter number of iterations:')
        
        work_lbl.grid(column=0,row=0)
        rest_lbl.grid(column=0,row=1)
        prep_lbl.grid(column=0,row=2)
        iterations_lbl.grid(column=0,row=3)
        
        work_entry = tk.Entry(parent,text='Enter work interval (seconds):')
        rest_entry = tk.Entry(parent,text='Enter rest interval (seconds):')
        prep_entry = tk.Entry(parent,text='Enter prep interval (seconds):')
        iterations_entry = tk.Entry(parent,text='Enter number of iterations:')
        
        work_entry.grid(column=1,row=0)
        rest_entry.grid(column=1,row=1)
        prep_entry.grid(column=1,row=2)
        iterations_entry.grid(column=1,row=3)
        
        work_entry.insert(0,60)
        rest_entry.insert(0,0)
        prep_entry.insert(0,3)
        iterations_entry.insert(0,10)
        
        lbl = tk.Label(parent,text='') #makes space for printout
        lbl.grid(row=6,columnspan=2) #places the Label so it displays
        
        
        def clicked(controller):
            res = {'text':'''Starting timer for {} iterations. \n Work interval: {} seconds
            Rest interval: {} seconds \n Prep time: {} seconds'''.format(iterations_entry.get(),
            work_entry.get(),rest_entry.get(),prep_entry.get()),
            'work':work_entry.get(),
            'rest':rest_entry.get(),
            'prep':prep_entry.get(),
            'num_its':iterations_entry.get()}
            lbl.configure(text=res['text'],anchor='w')
            print(res['text'])
            controller.show_frame(controller = TimerPage,kwargs=res)
        
        # Button widget
        btn = tk.Button(parent,text='Begin Work',
                        command=lambda: controller.show_frame(TimerPage))#,
#                                                              text='Starting timer for {} iterations. \n Work interval: {} seconds \n Rest interval: {} seconds \n Prep time: {} seconds'.format(iterations_entry.get(),
#                                                               work_entry.get(),rest_entry.get(),prep_entry.get()),
#            work=work_entry.get(),
#            rest=rest_entry.get(),
#            prep=prep_entry.get(),
#            num_its=iterations_entry.get()))
#                            clicked(controller)) #runs ```clicked``` when button pushed
        btn.grid(columnspan=2,row=5) #places button to display
        
        def update(self,*args,**kwargs):
            None
app = TabataApp()
app.mainloop()
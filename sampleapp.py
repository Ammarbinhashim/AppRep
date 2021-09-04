# a sample app that is just a footstep for a giant leap
'''
UPDATE: Just imported a new module(uix.widget)
.kv file will also be included


'''
from typing import Text
import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.lang import Builder

Builder.load_file('sample.kv')

class app_panel(Widget):
    pass


class grid(GridLayout):
    '''# I'll have to use the code down below if im going to define any app..
    # even working on a fucking grid or buttons..
    # or whatever the fuck that really is'''

    def __init__(self,**kwargs):
            super(grid,self).__init__(**kwargs)

             # Now the coloumns
             # Also I'll have to use self.<anything> befoe i do something wthin this block
             #Dont i forget indedntation right under the super statement bloke'''

             #rows and colums
             # i actuallyu had bigger rows and colums.
             # but i wanted to make it more organized for the time being.
             # so i use the top grid method.
             # THE SECOND GRID LAYOUT
            self.cols = 1

            #I can name any name for the grid layout.
            #for the time being ill call it chad

            self.chad = GridLayout()
            self.chad.cols = 2

            #Now gonna add chad into all the grids in the widgets down below
            #right after self

            self.yourname = TextInput(multiline=True,
            font_size=20,
            size_hint_x=None,
            size_hint_y=None,
            width = 400,
            height=50)

            self.chad.add_widget(self.yourname)
            self.chad.add_widget(Label(text="Name: ",
            font_size=20,
            size_hint_x=None,
            size_hint_y=None,
            width = 400,
            height=50))

            self.ppsize = TextInput(multiline=True,
            font_size=20,
            size_hint_x=None,
            size_hint_y=None,
            width = 400,
            height=50)

            self.chad.add_widget(self.ppsize)
            self.chad.add_widget(Label(text="Dick Size: ",
            font_size=20,
            size_hint_x=None,
            size_hint_y=None,
            width = 400,
            height=50))

            self.simpdetector = TextInput(multiline=True,
            font_size=20,
            size_hint_x=None,
            size_hint_y=None,
            width = 400,
            height=50)

            self.chad.add_widget(self.simpdetector)
            self.chad.add_widget(Label(text="You Gae?: ",
            font_size=20,
            size_hint_x=None,
            size_hint_y=None,
            width = 400,
            height=50))

            self.add_widget(self.chad)# The important part for top grid

            # So here i first added a button.
            # but i realized the fact that
            # it would look more dumb and cringe it
            # if i keep pressing it and does nothing
            # so i define a new function {def whattosay(self):} as its command
            # and then i'll bind this to the button using self.<button name>.bind statement
            # in the middle of these 2 statements down below
            #Now im actually trying to reduce the font size, and MAYBE the button size as well.

            '''Well i just realized the fact that you can use
            all these size_hint_x, size_hint_y, height, width
            on any widget.


            So now lemme go change the size of that ugly ass input panels

            '''

            self.approve = Button(text = "Conclusion:",
            size_hint_y =  None,
            height = 50, width = 150,
            size_hint_x= None,
            font_size=12)


            self.approve.bind(on_press = self.whattosay)
            self.add_widget(self.approve)

    def whattosay(self, instance):
        yourname = self.yourname.text
        ppsize = self.ppsize.text
        simpdetector = self.simpdetector.text

        # remeber to put an f down below.
        # This code literlly hates me
        # print(f"Hi {name}, your dick size is {ppsize} and {simpdetector}you are gae")
        self.add_widget(Label(text=f"Hi {yourname}, your dick size is {ppsize} and {simpdetector} you are gae"))


        ''' if some mfs click this over and over again,
         even when they see the fucking output
         for which i took 8 hours to build,
         this text will keep on recurring and its fucked..

         so this is JUST TO CLEAR OUT THE REST OF THE STATEMENT
         '''

        self.yourname.text = " "
        self.ppsize.text = " "
        self.simpdetector.text = " "

class SampleApp(App):
    def build(self):
        return grid()


SampleApp().run()

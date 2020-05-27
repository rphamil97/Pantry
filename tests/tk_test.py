from tkinter import *
from tkinter.ttk import *
import db_test

# we should have a way to enter recipes, view recipes (and make them), enter stocked food, view stocked food, create a grocery list

class Root(Tk):
    ''' Root class for GUI app '''

    def __init__(self, title = 'Pantry'):
        db_test.setup()
        # setup for GUI
        Tk.__init__(self)
        self.title(title)
        self.recipe_enter = Button(self, text = 'Enter Recipe', command = self.enter_recipe)
        self.recipe_view = Button(self, text = 'View Recipe', command = self.view_recipe)
        self.food_enter = Button(self, text = 'Enter Food', command = self.enter_food)
        self.food_view = Button(self, text = 'View Food', command = self.view_food)
        self.list_create = Button(self, text = 'Create Grocery List', command = self.create_list)

        # run GUI
        self.recipe_enter.pack()
        self.recipe_view.pack()
        self.food_enter.pack()
        self.food_view.pack()
        self.list_create.pack()

    def enter_recipe(self):
        # new window to enter recipe
        pass

    def view_recipe(self):
        pass

    def enter_food(self):
        # new window to enter food
        efw = Window('Enter Food')
        Label(efw, text = 'Name').grid(row = 0)
        efn = Entry(efw, name = 'food_name')
        efn.grid(row = 0, column = 1)
        Label(efw, text = 'Calories').grid(row = 1)
        efc = Entry(efw, name = 'food_calories')
        efc.grid(row = 1, column = 1)
        Label(efw, text = 'Servings').grid(row = 2)
        efs = Entry(efw, name = 'food_servings')
        efs.grid(row = 2, column = 1)
        Label(efw, text = 'Expiration Date').grid(row = 3)
        efe = Entry(efw, name = 'food_expiration')
        efe.grid(row = 3, column = 1)
        efw.submit.config(command = lambda:[db_test.insert('food', name = efn.get(), calories = efc.get(),
            servings = efs.get(), expiration_date = efe.get()), efw.destroy()])
        efw.submit.grid(row = 4)
        efw.close.grid(row = 4, column = 1)
        efw.mainloop()

    def view_food(self):
        # new window to view all foods
        print(self.efn.get())

    def create_list(self):
        pass

class Window(Toplevel):
    ''' Window class for simplifying window creation '''

    def __init__(self, title = 'Window'):
        Toplevel.__init__(self)
        self.title(title)
        self.submit = Button(self, text = 'Submit', command = lambda:[self.submit_call(), self.destroy()])
        self.close = Button(self, text = 'Close', command = self.destroy)

    def submit_call(self, **kwargs):
        """Is this a docstring?"""
        # print all entry names and values
        if 'func' in kwargs.keys():
            for key in kwargs:
                print(key + ': ' + kwargs[key])
        else:
            self.destroy()
            print('Function not specified')


def main():
    root = Root()
    root.mainloop()

if __name__ == '__main__':
    main()

from tkinter import *
import random


class App(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.radio = Frame(self)
        self.slide = Frame(self)
        self.mod_layer = Frame(self)
        self.text_options = Frame(self)
        self.text_layer = Frame(self)
        self.v = IntVar()
        self.mod_vals = IntVar()
        self.die_label = Label(self.radio, text='Pick a die value:')
        self.num_label = Label(self.slide, text='Number of dice to roll:')
        self.mod_label = Label(self.mod_layer, text='Roll modifier:')
        self.toggle_label = Label(self.text_options, text='Show modifiers')
        self.mod_vals_check = Checkbutton(self.text_options, variable=self.mod_vals)
        self.clear = Button(self.text_options, text='Clear', padx=20, command=self.clear)
        self.mod = Entry(self.mod_layer, width=6)
        self.long_text = Text(self.text_layer, width=40, height=4, state='disabled')
        self.radio_buttons = []
        self.dice = (4, 6, 8, 10, 12, 20, 100)
        for i, die in enumerate(self.dice):
            self.radio_buttons.append(Radiobutton(self.radio, text=f'D{die}', variable=self.v, value=i))
        self.scale = Scale(self.slide, from_=1, to=50, orient=HORIZONTAL)
        self.button = Button(self, text='Roll', padx=20, command=self.roll_dice)
        self.result = Label(self, text=0, relief="sunken", bg='white', padx=20, width=6, height=1)
        self.compile()

    def compile(self):
        self.pack(padx=10, pady=10)
        self.radio.pack(side='top')
        self.text_layer.pack(side='bottom')
        self.text_options.pack(side='bottom', anchor='w', pady=10)
        self.slide.pack(side='left')
        self.die_label.pack(anchor='w')
        self.num_label.pack()
        self.mod_label.pack(side='left')
        self.mod_layer.pack(pady=15)
        self.toggle_label.pack(side='left', ipadx=10)
        self.mod_vals_check.pack(side='left')
        self.clear.pack(side='right', padx=10)
        self.long_text.pack()
        self.mod.pack(side='left', padx=15)
        self.button.pack(side='left', padx=20)
        self.result.pack(side='left', padx=10)
        self.scale.pack(side='bottom', anchor='w', padx=10)
        for b in self.radio_buttons:
            b.pack(side='left', pady=10)
        self.v.set(5)

    def roll_dice(self):
        total = 0
        num_mod = 0
        vals = []
        if self.mod.get().isnumeric() or (self.mod.get()[1:].isnumeric() and self.mod.get()[0] in ('-', '+')):
            num_mod = int(self.mod.get())
        for roll in range(self.scale.get()):
            roll_val = random.randint(1, self.dice[self.v.get()])
            if self.mod_vals.get() and num_mod != 0:
                vals.append(f'{roll_val}({roll_val + num_mod})')
            else:
                vals.append(roll_val)
            total += roll_val
        if num_mod != 0:
            self.result['text'] = f'{total} {"+" if num_mod > 0 else "-"} {abs(num_mod)} = {total + num_mod}'
        else:
            self.result['text'] = f'{total}'
        self.long_text.configure(state='normal')
        self.long_text.insert('end', f'/{" ".join([str(i) for i in vals])}')
        self.long_text.configure(state='disabled')

    def clear(self):
        self.long_text.configure(state='normal')
        self.long_text.delete('1.0', END)
        self.long_text.configure(state='disabled')


root = Tk()
root.title('DND dice')
app = App(root)
mainloop()

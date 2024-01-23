import tkinter as tk
import tkinter.scrolledtext
m=tk.Tk()
m.title('chatbot')
tk.Grid()
conversation_lbl = tk.Label(m,anchor=tk.E,text='Conversation:')
conversation_lbl.grid(column=0, row=1, sticky='nesw', padx=3, pady=3)

conversation = tk.scrolledtext.ScrolledText(m, state='disabled')
conversation.grid(column=0, row=2, columnspan=2, sticky='nesw', padx=3, pady=3)
m.mainloop()
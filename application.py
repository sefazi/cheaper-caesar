import tkinter as tk
import method

class Application:
    def __init__(self):
        self.application = tk.Tk()
        self.input_frame = tk.Frame(self.application)
        self.input_frame.pack(padx=10, pady=10)

        # Input Message
        tk.Label(self.input_frame, text="Message:").grid(row=0, column=0, sticky=tk.W)
        self.message_entry = tk.Text(self.input_frame, height=4, width=50)
        self.message_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # Shift Entry
        tk.Label(self.input_frame, text="Shift:").grid(row=1, column=0, sticky=tk.W)
        self.shift_entry = tk.Entry(self.input_frame)
        self.shift_entry.grid(row=1, column=1, padx=5, pady=5)
        self.shift_entry.insert(0,"0")
        
        # Operation frame
        self.operation_frame = tk.Frame(self.application)
        self.operation_frame.pack(padx=10, pady=10)

        self.operation = tk.StringVar()
        self.operation.set("encrypt")
        
        # Radio Button
        tk.Radiobutton(self.operation_frame, text="Encrypt", variable=self.operation, value="encrypt").pack(side=tk.LEFT, padx=5)
        tk.Radiobutton(self.operation_frame, text="Decrypt", variable=self.operation, value="decrypt").pack(side=tk.LEFT, padx=5)
        
        # Button frame
        self.button_frame = tk.Frame(self.application)
        self.button_frame.pack(padx=10, pady=10)
        tk.Button(self.button_frame, text="Process",command=self.process_text).pack()
        
        # Result frame
        self.result_frame = tk.Frame(self.application)
        self.result_frame.pack(padx=10, pady=10)

        tk.Label(self.result_frame, text="Result:").pack(anchor=tk.W)
        self.result_text = tk.Text(self.result_frame, height=4, width=50, state=tk.DISABLED)
        self.result_text.pack(padx=5, pady=5)
        
    def process_text(self):
        method.process_text(self)
        
    def run(self):
        self.application.mainloop()
import tkinter as tk
from tkinter import ttk
import random
from PIL import Image, ImageTk
import os

class DiceRollingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("2 Dice Roller")
        self.root.geometry("600x400")
        self.root.resizable(True, True)
        
        self.bg_color = "#1a1a1a"  # Dark background
        self.accent_color = "#007acc"  # Blue accent
        self.text_color = "#ffffff"  # White text
        
        self.root.configure(bg=self.bg_color)
        
        # Create main frame
        self.main_frame = tk.Frame(root, bg=self.bg_color)
        self.main_frame.pack(expand=True, fill="both", padx=20, pady=20)
        
        # Title
        title_label = tk.Label(
            self.main_frame,
            text="2 Dice Roller",
            font=("Helvetica", 24, "bold"),
            bg=self.bg_color,
            fg=self.accent_color
        )
        title_label.pack(pady=20)
        
        # Dice Frame
        self.dice_frame = tk.Frame(self.main_frame, bg=self.bg_color)
        self.dice_frame.pack(expand=True, fill="both", pady=20)
        
        # Dice Results
        self.dice_result = tk.Label(
            self.dice_frame,
            text="? , ?",
            font=("Helvetica", 48, "bold"),
            bg=self.bg_color,
            fg=self.text_color
        )
        self.dice_result.pack(pady=20)
        
        # Roll Button
        self.style = ttk.Style()
        self.style.configure(
            "Accent.TButton",
            padding=10,
            background=self.accent_color,
            foreground='black'  
        )
        
        self.roll_button = ttk.Button(
            self.main_frame,
            text="ROLL DICE",
            style="Accent.TButton",
            command=self.roll_dice
        )
        self.roll_button.pack(pady=20)
        
        # Total Rolls Counter
        self.total_rolls = 0
        self.counter_label = tk.Label(
            self.main_frame,
            text="Total Rolls: 0",
            font=("Helvetica", 12),
            bg=self.bg_color,
            fg=self.accent_color
        )
        self.counter_label.pack(pady=10)
        
        # Bind resize event
        self.root.bind("<Configure>", self.on_resize)
    
    def roll_dice(self):
        # Disable button temporarily
        self.roll_button.state(["disabled"])
        self.root.after(100, self.perform_roll)
    
    def perform_roll(self):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        self.dice_result.config(text=f"{die1} , {die2}")
        
        # Update counter
        self.total_rolls += 1
        self.counter_label.config(text=f"Total Rolls: {self.total_rolls}")
        
        # Re-enable button
        self.roll_button.state(["!disabled"])
    
    def on_resize(self, event):
        # Update font sizes based on window size
        window_width = self.root.winfo_width()
        title_size = max(16, min(24, window_width // 25))
        dice_size = max(24, min(48, window_width // 12))
        
        for widget in self.main_frame.winfo_children():
            if isinstance(widget, tk.Label):
                if widget == self.dice_result:
                    widget.configure(font=("Helvetica", dice_size, "bold"))
                elif "CYBER DICE" in widget.cget("text"):
                    widget.configure(font=("Helvetica", title_size, "bold"))

if __name__ == "__main__":
    root = tk.Tk()
    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)
    except:
        pass
    
    app = DiceRollingApp(root)
    root.mainloop()

import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import time
import winsound

class DigitalClock(tk.Label):
    def __init__(self, root):
        super().__init__(root, font=('Helvetica', 48), bg='black', fg='white')
        self.pack(pady=20)
        self.update_time()

    def update_time(self):
        current_time = datetime.now().strftime('%H:%M:%S')
        self.config(text=current_time)
        self.after(1000, self.update_time)

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Timer")
        self.root.geometry("400x300")
        self.timer_running = False
        self.seconds_left = 0

        # Date Label
        self.date_label = tk.Label(root, text=datetime.now().strftime('%Y-%m-%d'), font=('Helvetica', 16))
        self.date_label.pack()

        self.timer_label = tk.Label(root, text="Timer: 00:00", font=('Helvetica', 24))
        self.timer_label.pack(pady=20)

        self.timer_entry_label = tk.Label(root, text="Set Timer (minutes):")
        self.timer_entry_label.pack()
        self.timer_entry = tk.Entry(root)
        self.timer_entry.pack()
        self.start_button = tk.Button(root, text="Start Timer", command=self.start_timer)
        self.start_button.pack()

        self.stop_button = tk.Button(root, text="Stop Timer", command=self.stop_timer, state=tk.DISABLED)
        self.stop_button.pack()

        # Created by Label
        self.created_by_label = tk.Label(root, text="Created by DinethH using Python 3 - 2023", font=('Helvetica', 10))
        self.created_by_label.pack(side=tk.BOTTOM)

    def start_timer(self):
        if not self.timer_running:
            try:
                minutes = int(self.timer_entry.get())
                self.seconds_left = minutes * 60
                self.timer_entry.config(state=tk.DISABLED)
                self.timer_running = True
                self.update_timer()
            except ValueError:
                pass  # Ignore invalid input

    def update_timer(self):
        if self.timer_running:
            minutes, seconds = divmod(self.seconds_left, 60)
            time_str = f"Timer: {minutes:02}:{seconds:02}"
            self.timer_label.config(text=time_str)
            if self.seconds_left > 0:
                self.seconds_left -= 1
                self.root.after(1000, self.update_timer)
            else:
                self.timer_running = False
                self.timer_entry.config(state=tk.NORMAL)
                self.start_button.config(state=tk.NORMAL)
                self.stop_button.config(state=tk.DISABLED)
                self.show_reminder()

    def stop_timer(self):
        self.timer_running = False
        self.timer_entry.config(state=tk.NORMAL)
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def show_reminder(self):
        messagebox.showinfo("Timer Reminder", "Time's up!")
        winsound.Beep(1000, 1000)  # Beep sound (frequency, duration)

class StopwatchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Timer Displayer")
        self.root.geometry("600x500")
        self.running = False
        self.start_time = 0

        # Date Label
        self.date_label = tk.Label(root, text=datetime.now().strftime('%Y-%m-%d'), font=('Helvetica', 16))
        self.date_label.pack()

        self.stopwatch_label = tk.Label(root, text="Stopwatch: 00:00", font=('Helvetica', 24))
        self.stopwatch_label.pack(pady=20)

        self.start_button = tk.Button(root, text="Start", command=self.start)
        self.stop_button = tk.Button(root, text="Stop", command=self.stop)
        self.reset_button = tk.Button(root, text="Reset", command=self.reset)

        self.start_button.pack()
        self.stop_button.pack()
        self.stop_button.config(state=tk.DISABLED)
        self.reset_button.pack()
        self.reset_button.config(state=tk.DISABLED)

        # Created by Label
        self.created_by_label = tk.Label(root, text="Created by DinethH using Python 3 - 2023", font=('Helvetica', 10))
        self.created_by_label.pack(side=tk.BOTTOM)

    def start(self):
        if not self.running:
            self.running = True
            self.start_time = time.time() - self.start_time
            self.update()

    def stop(self):
        if self.running:
            self.running = False
            self.stop_button.config(state=tk.DISABLED)
            self.start_button.config(text="Resume")
            self.reset_button.config(state=tk.NORMAL)

    def reset(self):
        self.running = False
        self.start_time = 0
        self.stopwatch_label.config(text="Stopwatch: 00:00")
        self.start_button.config(text="Start")
        self.reset_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

    def update(self):
        if self.running:
            elapsed_time = time.time() - self.start_time
            minutes, seconds = divmod(int(elapsed_time), 60)
            time_str = f"Stopwatch: {minutes:02}:{seconds:02}"
            self.stopwatch_label.config(text=time_str)
            self.root.after(1000, self.update)

def main():
    root = tk.Tk()
    root.title("Clock, Timer, and Stopwatch")
    root.geometry("800x500")
    root.configure(bg='black')

    clock = DigitalClock(root)
    timer = TimerApp(root)
    stopwatch = StopwatchApp(root)

    root.mainloop()

if __name__ == "__main__":
    main()

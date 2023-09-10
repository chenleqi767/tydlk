import tkinter as tk
from tkinter import ttk

def start_progress():
    progress_bar.start()  # 启动进度条

def stop_progress():
    progress_bar.stop()   # 停止进度条

def update_progress(value):
    progress_bar['value'] = value  # 更新进度条值

root = tk.Tk()

progress_bar = ttk.Progressbar(root, mode='determinate', length=200)  # 创建进度条
progress_bar.pack()

start_button = tk.Button(root, text="开始", command=start_progress)  # 创建开始按钮
start_button.pack()

stop_button = tk.Button(root, text="停止", command=stop_progress)  # 创建停止按钮
stop_button.pack()

update_button = tk.Button(root, text="更新", command=lambda: update_progress(50))  # 创建更新按钮
update_button.pack()

root.mainloop()
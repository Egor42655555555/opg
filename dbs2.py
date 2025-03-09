import tkinter as tk
from tkinter import messagebox
import sqlite3

def dbs():
    conn =
sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, phone TEXT NOT NULL, username TEXT NOT NULL UNIQUE, password TEXT NOT NULL)''')
    conn.commit()
    return conn

def register():
    phone = phone_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    
    conn = dbs()
    cursor = conn.cursor()
    
    try:
        cursor.execute('INSERT INTO users (phone, username, password) VAULES (?, ?, ?)', (phone, username, password))
        conn.commit()
messagebox.showinfo("registration", "registration successful")
  except sqlite3.intergrityerror:
      message.showerror("Error", "username already exists")
  finally:
      conn.close()
      
def login():
    username =
login_username_entry.get()
    password =
login_password_entry.get()
    
    conn = dbs()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    
    user = cursor.fetchone()
    if user:
        messagebox.showinfo("login", "login successful!")
    else:
        messagebox.chowerror("error", "invalid username or password")
        
        conn.close()
        
        
root = tk.TK()
root.title("registration and login")

tk.label(root, text="Phone").grid(row=0, column=0)
phone_entry = tk.Entry(root)
phone_entry.grid(row=0, column=1)

tk.label(root, text="username").grid(row=1, column=0)
username_entry = tk.Entry(root)
username_entry.grid(row=1, column=1)

tk.label(root, text="password").grid(row=2, column=0)
password_entry = tk.Entry(root)
password_entry.grid(row=2, column=1)


tk.Button(root, text="Register", command=register).grid(row=3, column=0, columnspan=2)

tk.label(root, text="login").grid(row=4, column=0, columnspan=2)

tk.label(root, text="username").grid(row=5, column=0)
login_username_entry = tk.Entry(root)
login_username_entry.grid(row=5, column=1)

tk.label(root, text="Password").grid(row=6, column=0)
login_password_entry = tk.Entry(root, show='*')
login_password_entry.grid(row=6, column=1)

tk.Button(root, text="login", command=login).grid(row=7, column=0, columnspan=2)

root.mainloop()
import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox

HOST = '192.168.1.82'
PORT = 12345

def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            chat_area.insert(tk.END, message + '\n')
            chat_area.yview(tk.END)
        except:
            messagebox.showerror("Error", "Conexión perdida con el servidor.")
            break

def send_message():
    message = f"{device_name}: {message_input.get()}"
    client_socket.send(message.encode('utf-8'))
    message_input.delete(0, tk.END)

try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
except Exception as e:
    messagebox.showerror("Error", f"No se pudo conectar al servidor: {e}")
    exit()

root = tk.Tk()
root.title("R3 Chat")

device_name = socket.gethostname()

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

chat_area = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=50, height=20, state='normal')
chat_area.pack()

message_input = tk.Entry(frame, width=40)
message_input.pack(side=tk.LEFT, padx=(0, 10))

send_button = tk.Button(frame, text="Enviar", command=send_message)
send_button.pack(side=tk.LEFT)

threading.Thread(target=receive_messages, daemon=True).start()

root.mainloop()

# Coded by R3-K1
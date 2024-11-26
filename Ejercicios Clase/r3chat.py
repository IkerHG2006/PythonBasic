import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox

# Configuración del cliente
HOST = '192.168.1.100'  # Cambia a la IP del servidor
PORT = 12345

# Función para recibir mensajes del servidor
def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            chat_area.insert(tk.END, message + '\n')
            chat_area.yview(tk.END)
        except:
            messagebox.showerror("Error", "Conexión perdida con el servidor.")
            break

# Enviar mensaje al servidor
def send_message():
    message = f"{device_name}: {message_input.get()}"
    client_socket.send(message.encode('utf-8'))
    message_input.delete(0, tk.END)

# Conectar al servidor
try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
except Exception as e:
    messagebox.showerror("Error", f"No se pudo conectar al servidor: {e}")
    exit()

# Interfaz gráfica
root = tk.Tk()
root.title("R3 Chat")

device_name = socket.gethostname()  # Obtener nombre del dispositivo

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

chat_area = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=50, height=20, state='normal')
chat_area.pack()

message_input = tk.Entry(frame, width=40)
message_input.pack(side=tk.LEFT, padx=(0, 10))

send_button = tk.Button(frame, text="Enviar", command=send_message)
send_button.pack(side=tk.LEFT)

# Hilo para recibir mensajes
threading.Thread(target=receive_messages, daemon=True).start()

root.mainloop()
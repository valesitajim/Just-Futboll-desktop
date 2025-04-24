import tkinter as tk
import subprocess
from datetime import datetime
import random
from tkinter import Label, Button, PhotoImage

def update_clock():
    now = datetime.now().strftime("%H:%M:%S")
    clock_label.config(text=now)
    root.after(1000, update_clock)

def open_shell():
    subprocess.Popen(["xterm", "-e", "bash /home/arturo/script1.sh"])

def open_web():
    try:
        subprocess.Popen(["xdg-open", "https://www.marca.com"])
    except Exception as e:
        print(f"Error al abrir la web: {e}")

def open_notas():
    notas_window = tk.Toplevel(root)
    notas_window.title("Notas")
    notas_window.geometry("400x300")
    notas_window.configure(bg="white")

    text_area = tk.Text(notas_window, wrap="word", font=("Arial", 12))
    text_area.pack(expand=True, fill="both", padx=10, pady=10)

    def guardar_notas():
        try:
            with open("notas.txt", "w") as file:
                file.write(text_area.get("1.0", "end-1c"))
            print("Notas guardadas correctamente.")
        except Exception as e:
            print(f"Error al guardar las notas: {e}")

    save_button = tk.Button(notas_window, text="Guardar Notas", command=guardar_notas, bg="lightgreen")
    save_button.pack(pady=5)

# Interfaz
root = tk.Tk()
root.title("ESCRITORIO JUSTFUTBALL")
root.geometry("800x600")

# Carga de imágenes
img_terminal = PhotoImage(file="terminal.png")
img_shell = PhotoImage(file="shell.png")
img_notas = PhotoImage(file="notas.png")
img_web = PhotoImage(file="html.png")  # Nueva imagen para el botón Web

canvas = tk.Canvas(root, width=800, height=600, bg='#2e8b57', highlightthickness=0)
canvas.pack()

canvas.create_line(400, 0, 400, 600, fill="white", width=2)
canvas.create_oval(350, 250, 450, 350, outline="white", width=2)
canvas.create_rectangle(0, 200, 50, 400, outline="white", width=2)
canvas.create_rectangle(750, 200, 800, 400, outline="white", width=2)

def create_soccer_ball(x, y, size):
    return canvas.create_oval(x-size, y-size, x+size, y+size, fill="white", outline="black")

ball_size = 20
ball_pos = [400, 300]
ball_speed = [random.choice([-4, -3, 3, 4]), random.choice([-4, -3, 3, 4])]
ball_obj = create_soccer_ball(ball_pos[0], ball_pos[1], ball_size)

def animate_ball():
    global ball_pos, ball_speed, ball_obj

    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    if ball_pos[0] <= ball_size or ball_pos[0] >= 800 - ball_size:
        ball_speed[0] = -ball_speed[0]
        ball_speed[1] += random.uniform(-1, 1)

    if ball_pos[1] <= ball_size or ball_pos[1] >= 600 - ball_size:
        ball_speed[1] = -ball_speed[1]
        ball_speed[0] += random.uniform(-1, 1)

    max_speed = 6
    for i in range(2):
        if abs(ball_speed[i]) > max_speed:
            ball_speed[i] = max_speed if ball_speed[i] > 0 else -max_speed

    canvas.delete(ball_obj)
    ball_obj = create_soccer_ball(ball_pos[0], ball_pos[1], ball_size)

    root.after(30, animate_ball)

clock_label = tk.Label(root, font=("Times new roman", 20), bg="#2e8b57", fg="white")
clock_label.place(x=600, y=20)
update_clock()

# Botones
tk.Button(root, text="Shell", image=img_shell, compound="top", command=open_shell, font=("Arial", 12)).place(x=50, y=150)
tk.Button(root, text="Notas", image=img_notas, compound="top", command=open_notas, font=("Arial", 12)).place(x=50, y=270)
tk.Button(root, text="Web", image=img_web, compound="top", command=open_web, font=("Arial", 12)).place(x=50, y=390)

animate_ball()

root.attributes('-fullscreen', False)
root.bind("<F11>", lambda event: root.attributes("-fullscreen", not root.attributes("-fullscreen")))
root.bind("<Escape>", lambda event: root.attributes("-fullscreen", False))

root.mainloop()

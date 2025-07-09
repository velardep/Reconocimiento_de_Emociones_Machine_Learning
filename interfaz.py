import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import threading

proc_reconocer = None

def centrar_ventana(ventana, ancho, alto):
    ventana.update_idletasks()
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()
    x = (ancho_pantalla // 2) - (ancho // 2)
    y = (alto_pantalla // 2) - (alto // 2)
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

def capturar_emociones():
    def lanzar_captura():
        emocion = combo.get()
        if emocion:
            ventana_emocion.destroy()
            subprocess.run(["python", "scripts/capturar_emociones.py", emocion])
        else:
            messagebox.showwarning("Advertencia", "Debes seleccionar una emoción.")

    ventana_emocion = tk.Toplevel(root)
    ancho_vent = 350
    alto_vent = 200
    ventana_emocion.title("Seleccionar emoción")
    ventana_emocion.minsize(300, 180)
    centrar_ventana(ventana_emocion, ancho_vent, alto_vent)

    for i in range(4):
        ventana_emocion.rowconfigure(i, weight=1)
    ventana_emocion.columnconfigure(0, weight=1)

    tk.Label(ventana_emocion, text="Selecciona una emoción:", font=("Arial", 12)).grid(row=0, column=0, pady=10)

    emociones = ["Felicidad", "Enojo", "Tristeza", "Sorpresa"]
    combo = ttk.Combobox(ventana_emocion, values=emociones, state="readonly", font=("Arial", 11))
    combo.grid(row=1, column=0, padx=30, sticky="ew")

    boton = tk.Button(ventana_emocion, text="Iniciar captura", command=lanzar_captura, font=("Arial", 11))
    boton.grid(row=2, column=0, pady=15, padx=50, sticky="nsew")

def entrenar_emociones():
    def tarea_entrenamiento():
        proceso = subprocess.run(
            ["python", "scripts/entrenamiento_emociones.py"],
            capture_output=True, text=True
        )
        salida = proceso.stdout
        root.after(0, lambda: mostrar_salida_entrenamiento(salida))

    text_salida.delete("1.0", tk.END)
    text_salida.insert(tk.END, "Entrenando...\n")
    threading.Thread(target=tarea_entrenamiento, daemon=True).start()

def mostrar_salida_entrenamiento(texto):
    text_salida.delete("1.0", tk.END)
    text_salida.insert(tk.END, texto)
    text_salida.see(tk.END)

def reconocer_emociones():
    global proc_reconocer
    if proc_reconocer is None or proc_reconocer.poll() is not None:
        proc_reconocer = subprocess.Popen(["python", "scripts/reconocimiento_emociones.py"])
    else:
        messagebox.showinfo("Info", "El reconocimiento ya está corriendo.")

def cerrar_reconocimiento():
    global proc_reconocer
    if proc_reconocer and proc_reconocer.poll() is None:
        proc_reconocer.terminate()
        proc_reconocer = None

def salir():
    cerrar_reconocimiento()
    root.destroy()

# --- Interfaz principal ---
root = tk.Tk()
ancho_principal = 600
alto_principal = 550
root.title("Sistema de Reconocimiento de Emociones")
root.geometry(f"{ancho_principal}x{alto_principal}")
root.minsize(500, 400)
centrar_ventana(root, ancho_principal, alto_principal)

root.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7], weight=1)
root.columnconfigure(0, weight=1)

tk.Label(root, text="Reconocimiento de Emociones", font=("Arial", 16)).grid(row=0, column=0, sticky="n", pady=10)

btn_capturar = tk.Button(root, text="Capturar Emociones", command=capturar_emociones)
btn_capturar.grid(row=1, column=0, sticky="nsew", padx=40, pady=5)

btn_entrenar = tk.Button(root, text="Entrenar Modelo", command=entrenar_emociones)
btn_entrenar.grid(row=2, column=0, sticky="nsew", padx=40, pady=5)

frame_text = tk.Frame(root)
frame_text.grid(row=3, column=0, sticky="nsew", padx=40, pady=5)
frame_text.rowconfigure(0, weight=1)
frame_text.columnconfigure(0, weight=1)

text_salida = tk.Text(frame_text, height=15, font=("Consolas", 10))
text_salida.grid(row=0, column=0, sticky="nsew")

scrollbar = tk.Scrollbar(frame_text, command=text_salida.yview)
scrollbar.grid(row=0, column=1, sticky="ns")
text_salida.config(yscrollcommand=scrollbar.set)

btn_reconocer = tk.Button(root, text="Reconocer Emociones", command=reconocer_emociones)
btn_reconocer.grid(row=4, column=0, sticky="nsew", padx=40, pady=5)

btn_cerrar_reconocimiento = tk.Button(root, text="Cerrar Reconocimiento", command=cerrar_reconocimiento, bg='blue', fg='white')
btn_cerrar_reconocimiento.grid(row=5, column=0, sticky="nsew", padx=40, pady=5)

btn_salir = tk.Button(root, text="Salir", command=salir, bg='red', fg='white')
btn_salir.grid(row=6, column=0, sticky="nsew", padx=40, pady=5)


root.mainloop()

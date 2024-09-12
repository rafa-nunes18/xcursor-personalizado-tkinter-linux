import tkinter as tk  
from tkinter import ttk  
import os   
import tkXcursor as tx

# Inicializando o aplicativo  
root = tk.Tk()  
root.title("Meu App de Cursores")  
cursors = []  


def my_load_cursors(widget, path):  
    global cursors    
    files = os.listdir(path)  
    for file in files:  
        file_path = os.path.join(path, file)  
        if os.path.isfile(file_path):        
            try:  
                cursor = tx.x_load_cursor(widget, file_path)    
                cursors.append(cursor)  
            except Exception as e:  
                print(f"Erro ao carregar {file_path}: {e}")  

def my_set_cursor(event, cursor_id):  
    """Define o cursor quando o mouse entra no botão."""  
    tx.x_set_cursor(event.widget, cursor_id)  

def reset_cursor(event):  
    """Remove o cursor quando o mouse sai do botão."""  
    # Restaurar o cursor padrão  
    default_cursor = "arrow"  # Ou outro cursor padrão que você deseja usar  
    event.widget.config(cursor=default_cursor)  

# Carregar os cursores usando um caminho relativo  
current_dir = os.path.dirname(__file__)  # Obtém o diretório atual do arquivo Python  
cursors_dir = os.path.join(current_dir, 'cursors')  # Constrói o caminho para a pasta cursors  
my_load_cursors(root, cursors_dir) # Certifique-se de que o caminho está correto  

# Criar botões para cada cursor  
for cursor in cursors:  
    button = ttk.Button(root, text='Hover over me for cursor', width=25)  
    button.pack(padx=5, pady=5)  

    # Usando um closure para garantir que o cursor correto é usado na função lambda  
    def set_cursor_for_button(cur):  
        button.bind('<Enter>', lambda event, cid=cur: my_set_cursor(event, cid))  
        button.bind('<Leave>', reset_cursor)  

    set_cursor_for_button(cursor)  

root.mainloop()
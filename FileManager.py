import customtkinter as ctk
import os
from tkinter import filedialog
from functools import partial
from Window import Window, ErrorWindow
from JsonManager import *

class FManager:
    def __init__(self, FPath):
        self.wf3 = Window("700x500", "Cyber File Manager")
        self.wf3.window.resizable(False, False)
        self.FPath = FPath
        self.current_path = self.FPath
        
        self.Loadedfiles = []
        self.create_menu()
        self.create_content_frame()
        self.load_files()
        
        self.wf3.Run()

    def create_content_frame(self):
        self.ContentFrame = ctk.CTkScrollableFrame(self.wf3.container, fg_color="#212121")
        self.ContentFrame.pack(fill="both", expand=True)
        self.ContentFrame.grid_columnconfigure(0, weight=1)

    def load_files(self):
        if self.current_path != self.FPath:
            self.returnBtn.place(x=600, y=1)
        else:
            self.returnBtn.place_forget()
        self.clear_container()
        for file in os.listdir(self.current_path):
            file_path = os.path.join(self.current_path, file)
            icon = "📁" if os.path.isdir(file_path) else "📄"
            btn = ctk.CTkButton(
                self.ContentFrame, 
                anchor="w",
                width=850,
                fg_color="#212121",
                text=f" {icon} {file}",
                font=("Arial", 20)
            )
            if not os.path.isdir(file_path):
                self.Loadedfiles.append(file)
            action = self.change_directory if os.path.isdir(file_path) else self.open_file
            btn.bind("<Double-Button-1>", partial(self.on_double_click, action, file_path))
            btn.pack(anchor="w", pady=1)
    
    def open_file(self, path):
        try:
            if os.name == "nt":
                os.startfile(path)
            else:
                os.system(f"open '{path}'")
        except Exception as e:
            ErrorWindow(f"No se pudo abrir el archivo: {e}")
    
    def new_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            open(file_path, 'w').close()
            self.load_files()
            
    def import_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            destination = os.path.join(self.current_path, os.path.basename(file_path))
            if not os.path.exists(destination):
                with open(file_path, 'rb') as src, open(destination, 'wb') as dst:
                    dst.write(src.read())
            self.load_files()

    def delete_file(self):
        file_path = filedialog.askopenfilename()
        if file_path and os.path.exists(file_path):
            os.remove(file_path)
            self.load_files()
            
    def on_double_click(self, action, path, event):
        action(path)

    def create_menu(self):
        menu_frame = ctk.CTkFrame(self.wf3.container, height=20, corner_radius=0, fg_color="gray10")
        menu_frame.pack(fill="x")

        self.create_dropdown(menu_frame, "File", 0, [
            ("New", self.new_file),
            ("Import", self.import_file),
            ("Delete", self.delete_file)
        ])

        self.create_dropdown(menu_frame, "Default Editor", 50, [
            ("Add Editor +",None),
        ])

        ctk.CTkLabel(menu_frame, text="Run File:",width=60, height=10).place(x=350, y=1)
        self.options = ["None","Change"]
        self.submenu = ctk.CTkOptionMenu(menu_frame,values=self.options,width=60, height=10,fg_color="#212121",command=self.setSubmenu)
        self.submenu.place(x=410, y=1)
        ctk.CTkButton(menu_frame, text="Set Run File", anchor="w", fg_color="gray10", width=60, height=10).place(x=240, y=1)
        self.searchbar=ctk.CTkEntry(menu_frame, width=200, height=2, placeholder_text="🔎  Search . . .", text_color="white")
        self.searchbar.place(x=150, y=1)
        self.searchbar.bind("<Return>", self.searchBar)
        self.returnBtn = ctk.CTkButton(menu_frame, text="<-- Return", anchor="w", fg_color="gray10", width=60, height=10,command=self.RetunrDir)
        self.returnBtn.place(x=600, y=1)

    def create_dropdown(self, parent, text, x_pos, options):
        dropdown_frame = ctk.CTkFrame(self.wf3.container, width=100, height=len(options) * 25, fg_color="gray20")
        dropdown_frame.place_forget()

        def toggle_dropdown():
            if dropdown_frame.winfo_ismapped():
                dropdown_frame.place_forget()
                dropdown_button.configure(fg_color="gray10")
            else:
                dropdown_frame.place(x=x_pos, y=21)
                dropdown_button.configure(fg_color="#14375e")
                dropdown_frame.lift()

        dropdown_button = ctk.CTkButton(parent, text=text, command=toggle_dropdown, fg_color="gray10", width=50, height=10)
        dropdown_button.place(x=x_pos, y=1)

        for opt_text, opt_command in options:
            ctk.CTkButton(dropdown_frame, text=opt_text, anchor="w", fg_color="gray20", width=120, height=10, command=opt_command).pack(pady=2)

    def clear_container(self):
        for widget in self.ContentFrame.winfo_children():
            widget.destroy()
     
    def setSubmenu(self,choice):
        if choice == "Change":
            jsonsFiles = JsonManager.JRead()
            for file in jsonsFiles:
                file_path = filedialog.askopenfilename(defaultextension="*.*", filetypes=[("Python Files", "*.py"),("C++ Files", "*.exe"),("Java Files", "*.Java/.Jar"), ("other", "*.*")])
                rpath = os.path.join(file_path.replace('/', '\\'))
                try:
                    jsonPath = f"{Create_JData.path}\\{file['name']}.json"
                    file.update({'RunFile':rpath})
                    JsonManager.JWrite(jsonPath,file)
                    self.options.append(f"{os.path.basename(rpath)}")
                    print(self.options)
                    self.submenu.configure(values=self.options)
                except Exception as e:
                    ErrorWindow(f"Error guardando archivo: {e}")
        elif choice == "None":
            jsonsFiles = JsonManager.JRead()
            for file in jsonsFiles:
                rpath = os.path.join(file_path.replace('/', '\\'))
                try:
                    jsonPath = f"{Create_JData.path}\\{file['name']}.json"
                    file.update({'RunFile':None})
                    JsonManager.JWrite(jsonPath,file)
                except Exception as e:
                    ErrorWindow(f"Error{e}")
        else:
            file = self.options[3]
            file.get({'RunFile':''})
            self.submenu.configure(values=self.options)
                       
    def RetunrDir(self):
        self.current_path = os.path.dirname(self.current_path)
        self.load_files()
        
    def change_directory(self, new_path):
        if os.path.isdir(new_path):
            self.current_path = new_path
            self.load_files()  

    def search(self):
        self.clear_container()
        query = self.searchbar.get().strip().lower()

        if not query:
            self.load_files()
            return

        results = []
        for root, dirs, files in os.walk(self.current_path):
            for name in dirs + files:
                if query in name.lower():
                    file_path = os.path.join(root, name)
                    results.append((file_path, name, os.path.isdir(file_path)))

        if results:
            for file_path, name, is_dir in results:
                icon = "📁" if is_dir else "📄"
                btn = ctk.CTkButton(self.ContentFrame,anchor="w",width=850,fg_color="#212121",text=f" {icon} {name}",font=("Arial", 20))
                action = self.change_directory if is_dir else self.open_file
                btn.bind("<Double-Button-1>", partial(self.on_double_click, action, file_path))
                btn.pack(anchor="w", pady=1)
        else:
            ctk.CTkLabel(self.ContentFrame, text="No se encontraron resultados", font=("Arial", 16)).pack(pady=20)

    def searchBar(self, event):
        self.search()
import customtkinter as ctk
from JsonManager import *
import os
from Window import Window,ErrorWindow
from tkinter import filedialog

class FManager():
    def __init__(self,FileName):
        self.wf3 = Window("700x400","Cyber File Manager")
        self.FileName = FileName
        self.Menu()
        self.Load()
        self.wf3.Run()

    def Load(self):
        for file in os.listdir(Create_JData.path):
            if file.endswith(".json"):
                json_file_path = os.path.join(Create_JData.path, file)
                data = None
                with open(json_file_path, "r") as f:
                    data = json.load(f)
                name = data["name"]
                project_path = data.get("Project_path", "")

                if self.FileName in name:
                    try:
                        os.path.join(json_file_path)
                    except PermissionError as e:
                        ErrorWindow(f"Error abriendo el proyecto: {e}")
                        return
                    if os.path.exists(project_path):
                        for root, dirs, files in os.walk(project_path, topdown=False):
                            for file_name in files:
                                file = os.path.join(root, file_name)
                                ctk.CTkButton(self.wf3.container,text=file).pack(pady=1)
                            for dir_name in dirs:
                                dir_to_remove = os.path.join(root, dir_name)
                                ctk.CTkButton(self.wf3.container,text=file).pack(pady=1)
                    break

    def Menu(self):
        menu_frame = ctk.CTkFrame(self.wf3.container, height=20, corner_radius=0, fg_color="gray10")  # Color de fondo
        menu_frame.pack(fill="x")
        def show_dropdown():
            if dropdown_frame.winfo_ismapped():
                dropdown_frame.place_forget()
                dropdown_button.configure(fg_color="gray10")
            else:
                dropdown_frame.place(x=0, y=21)
                dropdown_button.configure(fg_color="#14375e")
                if dropdown_frame2.winfo_ismapped():
                    dropdown_frame2.place_forget()
                    dropdown_button2.configure(fg_color="gray10")
        dropdown_button = ctk.CTkButton(menu_frame, text="File", command=show_dropdown,fg_color="gray10",bg_color="gray10", width=50, height=10)
        dropdown_button.place(x=0, y=1)
        dropdown_frame = ctk.CTkFrame(self.wf3.container, width=100, height=60, fg_color="gray20")
        dropdown_frame.place_forget()
        def show_dropdown2():
            if dropdown_frame2.winfo_ismapped():
                dropdown_frame2.place_forget()
                dropdown_button2.configure(fg_color="gray10")
            else:
                dropdown_frame2.place(x=50, y=21)
                dropdown_button2.configure(fg_color="#14375e")
                if dropdown_frame.winfo_ismapped():
                    dropdown_frame.place_forget()
                    dropdown_button.configure(fg_color="gray10")
        dropdown_button2 = ctk.CTkButton(menu_frame, text="Default Editor", command=show_dropdown2,fg_color="gray10",bg_color="gray10", width=50, height=10)
        dropdown_button2.place(x=50, y=1)
        dropdown_frame2 = ctk.CTkFrame(self.wf3.container, width=200, height=60, fg_color="gray20")
        dropdown_frame2.place_forget()
        
        ctk.CTkButton(dropdown_frame, text="New", anchor="w",fg_color="gray20",width=120,height=10).pack(pady=2)
        ctk.CTkButton(dropdown_frame, text="Import",anchor="w",fg_color="gray20",width=120,height=10).pack(pady=2)
        ctk.CTkButton(dropdown_frame, text="Delete",anchor="w",fg_color="gray20",width=120,height=10).pack(pady=2)
        
        b1 = ctk.CTkButton(menu_frame, text="Set Run File",anchor="w",fg_color="gray10",width=60,height=10).place(x=150, y=1)
        searchBar = ctk.CTkEntry(menu_frame, width=200,height=2,placeholder_text="🔎  Search . . .",text_color="white").place(x=240,y=1)
    
    
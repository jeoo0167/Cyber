import customtkinter as ctk
import os
from JsonManager import *
from PIL import Image
from Window import ErrorWindow, Window, deleteWindow
from FileManager import FManager
class Functions:
    def __init__(self, window,canvas,dataList):
        self.window = window
        self.canvas = canvas
        self.datalist = dataList
        self.indexId = []
    def Rectangle(self, x, y,w,h):
        x0 = x
        y0 = y
        x1 = x0 + w
        y1 = y0 + h

        self.canvas.create_rectangle(x0, y0, x1, y1, outline="white",width=5)

    def clear(self):
        self.canvas.delete("all")
    def DataTag(self, img_path, name, desc, type, date, y):

        self.Rectangle(20, y, 920, 200) 
        
        img = ctk.CTkImage(light_image=Image.open(self.window.get_asset_path(img_path)), size=(150, 150))
        label_img = ctk.CTkLabel(self.canvas, image=img, text="")
        self.canvas.create_window(125, y + 100, window=label_img)

        label_name = ctk.CTkLabel(self.canvas, text=name, font=("Arial", 20, 'bold'))
        self.canvas.create_window(310, y + 20, window=label_name)

        label_desc = ctk.CTkLabel(self.canvas, text="Description", font=("Arial", 20, 'bold'))
        self.canvas.create_window(620, y + 20, window=label_desc)
        
        label_date = ctk.CTkLabel(self.canvas, text=date, font=("Arial", 12, 'bold'))
        self.canvas.create_window(500, y + 180, window=label_date)
        
        label_type = ctk.CTkLabel(self.canvas, text=type, font=("Arial", 15, 'bold'))
        self.canvas.create_window(320, y + 180, window=label_type)
        textbox = ctk.CTkTextbox(self.canvas, width=300, height=100, fg_color="black", bg_color="#333333")
        textbox.configure(state="normal")
        textbox.insert("end", desc)
        textbox.configure(state="disabled")
        self.canvas.create_window(650, y + 110, window=textbox)

        btn_manage = ctk.CTkButton(self.canvas, text="Manage", width=50,command=lambda:FManager(self.GetPath()))
        self.canvas.create_window(280, y + 80, window=btn_manage)

        btn_open = ctk.CTkButton(self.canvas, text="  Open  ", width=50)
        self.canvas.create_window(280, y + 120, window=btn_open)

        btn_run = ctk.CTkButton(self.canvas, text="  Run  ",text_color="White", width=50,command=lambda:self.IsRun())
        self.canvas.create_window(360, y + 120, window=btn_run)

        btn_delete = ctk.CTkButton(self.canvas, text="Delete", width=50,command=lambda:self.remove(name))
        self.canvas.create_window(360, y + 80, window=btn_delete)
        
        select = ctk.CTkCheckBox(self.canvas, text="", width=0)
        self.canvas.create_window(880, y + 110, window=select)
        self.Rectangle(20, y, 200, 200)

    def update_scrollregion(self):
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def Get(self):
        """Carga y muestra todos los proyectos en el canvas."""
        self.scrollbar = ctk.CTkScrollbar(self.window.container, command=self.canvas.yview)
        self.scrollbar.place(x=1000, y=100)
        self.scrollWidth = 200
        self.canvas.config(scrollregion=(0, 0, 0, 0))
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        y_position = 20

        for data in self.datalist:
            description = data.get("Description", "No description available")
            self.DataTag(
                data.get("Icon_path", "N/A"), 
                data.get("name", "Unnamed"), 
                description, 
                data.get("Type", "Unknown"), 
                data.get("date", "Unknown"), 
                y_position
            )
            self.indexId.append(data.get("name"))
            y_position += 220
            self.scrollWidth += 200
            self.canvas.config(scrollregion=(0, 0, 0, self.scrollWidth))

        if not self.datalist:
            ctk.CTkLabel(self.canvas,text="no projects found").place(x=0,y=20)
    def GetPath(self):
        """Devuelve la ruta del proyecto seleccionado."""
        for data in self.datalist:
            return data.get("Project_path", "Error")
    
    def searchBy(self, index="",element=""):
        self.clear()
        y_position = 20
        for data in self.datalist:
            name = data[element].lower() if data[element] else ""
            description = data.get("Description", "No description available").lower() if data.get("Description") else "no description available"
            if index in name:
                self.DataTag(data["Icon_path"], data["name"], description, data["Type"], data["date"], y_position)
                y_position += 220
        self.update_scrollregion()
        
    def remove_obj(self, Currentname):
        for file in os.listdir(Create_JData.path):
            if file.endswith(".json"):
                json_file_path = os.path.join(Create_JData.path, file)
                data = None
                with open(json_file_path, "r") as f:
                    data = json.load(f)
                name = data["name"]
                description = data.get("Description", "No description available").lower()
                project_path = data.get("Project_path", "")

                if Currentname in name or Currentname in description:
                    self.clear()
                    self.indexId.pop(self.indexId.index(name))
                    try:
                        os.remove(json_file_path)
                    except PermissionError as e:
                        ErrorWindow(f"Error eliminando el archivo JSON: {e}")
                        return
                    if os.path.exists(project_path):
                        try:
                            for root, dirs, files in os.walk(project_path, topdown=False):
                                for file_name in files:
                                    file_to_remove = os.path.join(root, file_name)
                                    os.remove(file_to_remove)
                                for dir_name in dirs:
                                    dir_to_remove = os.path.join(root, dir_name)
                                    os.rmdir(dir_to_remove)
                            os.rmdir(project_path)
                        except Exception as e:
                            ErrorWindow(f"Error eliminando el directorio del proyecto: {e}")
                            return
                    break

    def remove(self, currentname):
        deleteWindow(currentname,lambda: self.remove_obj(currentname))
        self.Get()
    def IsRun(self):
        for data in self.datalist:
            try:
                if data.get("RunFile"):
                    os.startfile(data.get("RunFile"))
            except Exception as e:
                ErrorWindow(f"Error al abrir el archivo: {e}")
                return

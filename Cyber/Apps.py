from Window import Window,ErrorWindow,AlertWindow
from functions import Functions
from tkinter import filedialog
import customtkinter as ctk
from PIL import Image
from JsonManager import *
from Samples import *
import os

class Create():
    def __init__(self):
        self.w1 = Window("1200x600","Cyber")
        result = self.w1.imgLoad()
        if isinstance(result, str):
            ErrorWindow(f"Error cargando imagenes {result}")
        else:
            self.images = result
            self.MainWindow()
        self.w1.Run()

    def MainWindow(self):
        tx1 = ctk.CTkLabel(self.w1.container, text="   Welcome to Cyber!", text_color="white", font=("Arial", 60, 'bold'))
        tx1.place(x=300, y=20)
        tx2 = ctk.CTkLabel(self.w1.container, text="Select a project Template", text_color="white", font=("Arial",25))
        tx2.place(x=470, y=100)
        self.images["img1"] = ctk.CTkImage(light_image=Image.open(self.w1.get_asset_path("Img1.png")), size=(200, 200))
        self.images["img2"] = ctk.CTkImage(light_image=Image.open(self.w1.get_asset_path("Img2.png")), size=(200, 200))
        self.images["img3"] = ctk.CTkImage(light_image=Image.open(self.w1.get_asset_path("Img3.png")), size=(200, 200))
        
        b1 = ctk.CTkButton(self.w1.container, width=200,height=200,image=self.images["img1"], text="",fg_color="#333333", command=lambda: self.B6())
        b1.place(x=60, y=250)
        b2 = ctk.CTkButton(self.w1.container, width=200,height=200,image=self.images["img2"], text="",fg_color="#333333", command=lambda: self.B1())
        b2.place(x=480, y=250)
        b3 = ctk.CTkButton(self.w1.container,width=200,height=200,image=self.images["img3"], text="",fg_color="#333333", command=lambda: self.ProgramingWindow())
        b3.place(x=870, y=250)
        ctk.CTkLabel(self.w1.container, text="   Mechatronic", text_color="white", font=("Arial", 35, 'bold')).place(x=60, y=520)
        ctk.CTkLabel(self.w1.container, text="     Electronic", text_color="white", font=("Arial", 35, 'bold')).place(x=480, y=520)
        ctk.CTkLabel(self.w1.container, text="  Programming", text_color="white", font=("Arial", 35, 'bold')).place(x=870, y=520)
    def ProgramingWindow(self):
        dx,dy = 360 ,150
        dx1,dy1 = 620, 150
        self.w1.Clear()
        tx4 = ctk.CTkLabel(self.w1.container, text="   Welcome to Cyber!", text_color="white", font=("Arial", 60, 'bold'))
        tx4.place(x=300, y=20)
        tx5 = ctk.CTkLabel(self.w1.container, text="Select a project Template", text_color="white", font=("Arial",25))
        tx5.place(x=470, y=100)
        
        b4 = ctk.CTkButton(self.w1.container, width=50,height=50,image=self.images["Python_logo"], text="",fg_color="#333333",command=lambda:self.B2())
        b4.place(x=dx, y=dy)
        b5 = ctk.CTkButton(self.w1.container, width=50,height=50,image=self.images["C++_logo"], text="",fg_color="#333333",command=lambda:self.B3())
        b5.place(x=dx1, y=dy1)
        b5 = ctk.CTkButton(self.w1.container, width=150,height=150,image=self.images["Java"], text="",fg_color="#333333",command=lambda:self.B5())
        b5.place(x=dx, y=dy+250)
        b7 = ctk.CTkButton(self.w1.container,width=50,height=50,image=self.images["Web_Dev"], text="",fg_color="#333333",command=lambda:self.B4())
        b7.place(x=dx1, y=dy1+250)
        ctk.CTkLabel(self.w1.container, text="Python", text_color="white", font=("Arial", 35, 'bold')).place(x=160, y=210)
        ctk.CTkLabel(self.w1.container, text="  Java", text_color="white", font=("Arial", 35, 'bold')).place(x=160, y=480)
        ctk.CTkLabel(self.w1.container, text="  C++", text_color="white", font=("Arial", 35, 'bold')).place(x=860, y=210)
        ctk.CTkLabel(self.w1.container, text="  Web\n Development", text_color="white", font=("Arial", 35, 'bold')).place(x=870, y=440)
    def B1(self):
        self.w1.window.destroy()
        ElectronicConf()
    def B2(self):
        self.w1.window.destroy()
        PythonConf()
    def B3(self):
        self.w1.window.destroy()
        C_Conf()
    def B4(self):
        self.w1.window.destroy()
        Web_Conf()
    def B5(self):
        self.w1.window.destroy()
        JavaConf()
    def B6(self):
        self.w1.window.destroy()
        MechatronicConf()
        
class Hub():
    def __init__(self):
        self.w1 = Window("1200x600", "Cyber")
        result = self.w1.imgLoad()

        self.data_list = JsonManager.JRead()
        self.canvas = ctk.CTkCanvas(self.w1.container, width=990, height=800, bg="#333333", highlightthickness=0)
        self.canvas.place(x=255, y=100)
        self.bgcanvas = ctk.CTkCanvas(self.w1.container, width=240, height=800, bg="#333333", highlightthickness=0)
        self.bgcanvas.place(x=0, y=0)
        self.program = Functions(self.w1, self.canvas,self.data_list)
        
        if isinstance(result, str):
            ErrorWindow(f"Error cargando imágenes {result}")
        else:
            self.images = result
        self.MainContent()
        self.program.Get()
        self.w1.Run()
        
        if not os.path.exists(Create_JData.path):
            os.system(f"mkdir {Create_JData.path}")
    
    def MainContent(self):
        self.searchBar = ctk.CTkEntry(self.w1.container, width=800,placeholder_text="🔎  Search . . .",text_color="white")
        self.searchBar.place(x=200, y=20)
        self.searchBar.bind("<Return>", self.search)
        images = [
            ctk.CTkImage(light_image=Image.open(self.w1.get_asset_path("Img1.png")), size=(80, 80)),
            ctk.CTkImage(light_image=Image.open(self.w1.get_asset_path("Img2.png")), size=(80, 80)),
            ctk.CTkImage(light_image=Image.open(self.w1.get_asset_path("Img3.png")), size=(80, 80))
        ]
        ctk.CTkButton(self.w1.container, text="≣  All", font=("Arial", 40, 'bold'), fg_color="#333333",bg_color="#333333",command= lambda:self.program.Get()).place(x=0, y=40)
        ctk.CTkButton(self.w1.container, text="Mechatronics", image=images[1], fg_color="#333333",bg_color="#333333",command=lambda:self.program.searchBy("mechatronic window", "Index")).place(x=0, y=100)
        ctk.CTkButton(self.w1.container, text="Electronics", image=images[0], fg_color="#333333",bg_color="#333333",command=lambda:self.program.searchBy("electronic window", "Index")).place(x=0, y=200)
        ctk.CTkButton(self.w1.container, text="Programing", image=images[2], fg_color="#333333",bg_color="#333333",command=lambda:self.program.searchBy("programing window", "Index")).place(x=0, y=300)
        ctk.CTkButton(self.w1.container, text="+ New Project", fg_color="#333333", command=self.goTo).place(x=1050, y=50)
        ctk.CTkButton(self.w1.container, text="+ Import project",command=self.GetimportProject, fg_color="#333333").place(x=1050, y=100)

    def GetimportProject(self):
        try:
            self.project = filedialog.askopenfilename(filetypes=[("Json files", "*.json")])
            if self.project == "":
                return
            with open(self.project, "r") as f:
                self.program.Get()
                data = json.loads(f.read())
                Create_JData(data["name"],data["Description"],data["Project_path"],data["Icon_path"],data["Files_path"],data["Files"],data["Asset Folder name"])
                self.program.indexId.append(data["name"])
                print(self.program.indexId)
        except Exception as e:
            if e == "name":
                ErrorWindow("Error importando el proyecto: El nombre del proyecto ya existe")
            elif e == "path":
                ErrorWindow("Error importando el proyecto: El directorio del proyecto ya existe")
            elif e == "list indices must be integers or slices, not str":
                ErrorWindow("Error importando el proyecto: El archivo seleccionado no es un proyecto")
            else:
                ErrorWindow(f"Error importando el proyecto: {e}")
        self.program.Get()
    def goTo(self):
        self.w1.window.destroy()
        Create()
    
    def search(self,event):
        self.program.searchBy(self.searchBar.get(),"name")


    def get_project_data(self, project_name):
        for file in os.listdir(Create_JData.path):
            if file.endswith(".json"):
                json_file_path = os.path.join(Create_JData.path, file)
                with open(json_file_path, "r") as f:
                    data = json.load(f)
                if data["name"] == project_name:
                    return data
        return None
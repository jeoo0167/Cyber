import customtkinter as ctk
import os,json
from PIL import Image
from tkinter import filedialog
from JsonManager import Create_JData

class Window():
    def __init__(self,Size,title):
        ctk.set_default_color_theme("dark-blue")
        ctk.set_appearance_mode("dark")
        self.window = ctk.CTk()
        self.window.geometry(Size)
        self.container = ctk.CTkFrame(self.window,bg_color="#333333")
        self.container.pack(fill=ctk.BOTH, expand=True)
        self.window.iconbitmap('Assets\\CyberLogo.ico')
        self.window.title(title)
    def get_asset_path(self, filename):
        return os.path.join(os.getcwd(), "Assets", filename)
    def imgLoad(self):
        try:
            images = {
                "img1": ctk.CTkImage(light_image=Image.open(self.get_asset_path("Img1.png")), size=(250, 250)),
                "img2": ctk.CTkImage(light_image=Image.open(self.get_asset_path("Img2.png")), size=(250, 250)),
                "img3": ctk.CTkImage(light_image=Image.open(self.get_asset_path("Img3.png")), size=(250, 250)),
                "Python_logo": ctk.CTkImage(light_image=Image.open(self.get_asset_path("Python_logo.png")), size=(150, 150)),
                "Web_Dev": ctk.CTkImage(light_image=Image.open(self.get_asset_path("Web_Dev.png")), size=(150, 150)),
                "C++_logo": ctk.CTkImage(light_image=Image.open(self.get_asset_path("C++_logo.png")), size=(150, 150)),
                "Code": ctk.CTkImage(light_image=Image.open(self.get_asset_path("Code.png")), size=(250, 250)),
                "3D": ctk.CTkImage(light_image=Image.open(self.get_asset_path("3D.png")), size=(250, 250)),                                     
                "imgSample": ctk.CTkImage(light_image=Image.open(self.get_asset_path("CyberLogo.png")), size=(125, 125)),
                "Java": ctk.CTkImage(light_image=Image.open(self.get_asset_path("Java_logo.png")), size=(150, 150))
            }
            return images
        except Exception as e:
            return str(e)
    def Run(self):
        self.window.mainloop()
    def Clear(self):
        for widget in self.container.winfo_children():
            widget.destroy()        
class ErrorWindow(Window):        
    def __init__(self, error):
        super().__init__("600x200", "Error")
        frame = ctk.CTkFrame(self.container)
        frame.pack(padx=10, pady=10, fill="both", expand=True)
        
        tx1 = ctk.CTkTextbox(frame, width=560, height=160, fg_color="black", text_color="yellow", font=("Arial", 20, "bold"), wrap="none")
        tx1.grid(row=0, column=0, sticky="nsew")
        tx1.insert("1.0", error)
        tx1.configure(state="disabled")  
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)
class AlertWindow(Window):
    def __init__(self,title, message,size=None):
        default_size = "400x150"
        super().__init__(size if size else default_size, title)
        ctk.CTkLabel(self.container, text=message, font=("Arial", 20, 'bold')).place(x=20, y=20)
        ctk.CTkButton(self.container, width=50, text="Ok", command=self.window.destroy).place(x=250, y=100)
        self.Run()
class deleteWindow(Window):
    def __init__(self, Currentname, on_confirm):
        super().__init__("600x200", f"Delete {Currentname}?")
        self.on_confirm = on_confirm
        ctk.CTkLabel(self.container, text=f"Are you sure you want to delete '{Currentname}'?", font=("Arial", 20, 'bold')).place(x=20, y=20)
        self.yesBtn = ctk.CTkButton(self.container, width=50, text="Yes", command=self.confirm_deletion)
        self.yesBtn.place(x=100, y=100)
        ctk.CTkButton(self.container, width=50, text="No", command=self.window.destroy).place(x=200, y=100)
        self.Run()
    def confirm_deletion(self):
        self.on_confirm()
        self.window.destroy()

class ConfigWindow(Window):
    def __init__(self,title):
        super().__init__("600x700",title)
        self.canvas = ctk.CTkCanvas(self.container, width=745, height=890,bg="#333333",highlightthickness=0)
        self.canvas.place(x=0,y=0)    
        self.canvas.create_rectangle(20, 5, 205, 180,outline="white", width=4)
        
        result = self.imgLoad()
        if isinstance(result, str):
            ErrorWindow(f"Error cargando imagenes {result}")
        else:
            self.images = result
            self.img = ctk.CTkLabel(self.container, text="",image=self.images["imgSample"],bg_color="#333333")
            self.img.place(x=25,y=15)
        self.CreatedFiles =[]
        self.AddedFiles =[]
        self.Assets=[]
        self.count = 0
        self.PathChanged = False
        self.count2 = 0
        self.img_path = None
        self.GlobalPath = f"{os.path.expanduser('~')}\\Documentos\\CyberProjects"
        self.interface()
        self.ExternalContent()
        self.getCheckbox()
        self.Run()
    def create_checkboxes(self, labels, positions, update_method):
        self.vars = [ctk.IntVar() for _ in labels]
        self.checkboxes = []
        for i, label in enumerate(labels):
            checkbox = ctk.CTkCheckBox(
                self.container,
                text=label,
                bg_color="#333333",
                variable=self.vars[i],
                onvalue=1,
                offvalue=0,
                command=lambda index=i: update_method(index),
            )
            checkbox.place(x=positions[i][0], y=positions[i][1])
            self.checkboxes.append(checkbox)

    def update_checkboxes(self, index):
        for i, var in enumerate(self.vars):
            var.set(1 if i == index else 0)

    def interface(self):
        self.inp1 = ctk.CTkEntry(self.container, width=160, height=25, placeholder_text="Project Name", fg_color="WHITE", text_color="BLACK",bg_color="#333333")
        self.inp1.place(x=10,y=150)
        ctk.CTkLabel(self.container,text="Project path",bg_color="#333333").place(x=210,y=480)
        self.path_inp1 = ctk.CTkTextbox(self.container, width=360, height=15, fg_color="WHITE", text_color="BLACK",bg_color="#333333")
        self.path_inp1.place(x=210,y=505)
        self.path_inp1.insert("1.0", self.GlobalPath)
        self.path_inp1.configure(state="disabled")
  
        ctk.CTkLabel(self.container,text="Assets folder name",bg_color="#333333").place(x=210,y=420)
        self.inp2 = ctk.CTkEntry(self.container, width=160, height=25, placeholder_text="Assets", fg_color="WHITE", text_color="BLACK",bg_color="#333333")
        self.inp2.place(x=210,y=450)
        btn = ctk.CTkButton(self.container, width=220, text="Create Files+",bg_color="#333333", command=self.AddFile)
        btn.place(x=190, y=90)
        btn2 = ctk.CTkButton(self.container, width=100, text="Add Files+",bg_color="#333333", command=self.OpenFile)
        btn2.place(x=190, y=10)
        btn2_1 = ctk.CTkButton(self.container, width=100, text="Remove file-",bg_color="#333333", command=self.RemoveFile)
        btn2_1.place(x=190, y=50)
        btn2_2 = ctk.CTkButton(self.container, width=100, text="Add Asset+",bg_color="#333333", command=self.OpenAsset)
        btn2_2.place(x=310, y=10)
        btn2_3 = ctk.CTkButton(self.container, width=100, text="Remove Asset-",bg_color="#333333", command=self.RemoveAsset)
        btn2_3.place(x=310, y=50)
        btn3 = ctk.CTkButton(self.container, width=160, text="Change icon",bg_color="#333333", command=self.Changeicon)
        btn3.place(x=10,y=180)
        self.btn4 = ctk.CTkButton(self.container, width=120, height=40,text="Create!",fg_color="green",command=self.createBtn)
        self.btn4.place(x=480, y=660)
        ctk.CTkLabel(self.container,text="Files",bg_color="#333333",font=("Arial",20,'bold')).place(x=120,y = 220)
        self.tbx1 = ctk.CTkTextbox(self.container, width=280, height=150, fg_color="black", text_color="white", font=("Arial", 14, "bold"))
        self.tbx1.place(x=10, y=260)  
        self.tbx1.configure(state="disabled")
        ctk.CTkLabel(self.container,text="Assets",bg_color="#333333",font=("Arial",20,'bold')).place(x=400,y=220)
        self.tbx2 = ctk.CTkTextbox(self.container, width=280, height=150, fg_color="black", text_color="white", font=("Arial", 14, "bold"))
        self.tbx2.place(x=310, y=260) 
        self.tbx2.configure(state="disabled")
        ctk.CTkLabel(self.container,text="Description",bg_color="#333333",font=("Arial",12)).place(x=210,y=540)
        self.tbx3 = ctk.CTkTextbox(self.container, width=360, height=75, fg_color="white", text_color="black", font=("Arial", 14, "bold"))
        self.tbx3.place(x=210, y=570)
        self.tbx3.configure(state="normal")
        self.pathBtn = ctk.CTkButton(self.container, width=100, text="ChangePath",font=("Arial", 14),command=self.Change_path)
        self.pathBtn.place(x=470, y=450)
        
    def ExternalContent(self):
        pass
    def AddFile(self):
        if not hasattr(self, "scroll"):
            self.scroll = ctk.CTkScrollableFrame(self.container,width=160,height=10,fg_color="#333333")
            self.scroll.place(x=10, y=420)
            self.scroll.grid_columnconfigure(0, weight=1)
        inpF = ctk.CTkEntry(self.scroll, width=150, height=25, placeholder_text=f"New File {self.count + 1}", fg_color="WHITE", text_color="BLACK")
        inpF.grid(row=self.count, column=0, padx=10, pady=5, sticky="w")
        self.CreatedFiles.append(inpF)

        self.count += 1
        
    def OpenFile(self):
        self.file_path = filedialog.askopenfilename(title="Select file", filetypes=[("Todos los archivos", "*.*")])
        if self.file_path:
            self.tbx1.configure(state="normal")
            self.tbx1.insert("end", self.file_path + "\n")
            self.tbx1.configure(state="disabled") 
            dir = os.path.join(self.file_path.replace('/', '\\'))
            self.AddedFiles.append(dir)
    def OpenAsset(self):
        self.file_path = filedialog.askopenfilename(title="Select asstes", filetypes=[("Todos los archivos", "*.*")])
        if self.file_path:
            self.tbx2.configure(state="normal")
            self.tbx2.insert("end", self.file_path + "\n")
            self.tbx2.configure(state="disabled") 
            dir = os.path.join(self.file_path.replace('/', '\\'))
            self.Assets.append(dir)
    def RemoveAsset(self): 
        if not self.Assets:
            return
        self.Assets.pop()  

        self.tbx2.configure(state="normal")
        self.tbx2.delete("1.0", "end")

        for file in enumerate(self.Assets, start=1):
            self.tbx2.insert("end", f"{file}\n")

        self.tbx1.configure(state="disabled")
    def RemoveFile(self): 
        if not self.AddedFiles:
            return
        self.AddedFiles.pop()  

        self.tbx1.configure(state="normal")
        self.tbx1.delete("1.0", "end")

        for file in enumerate(self.AddedFiles, start=1):
            self.tbx1.insert("end", f"{file}\n")

        self.tbx1.configure(state="disabled")

    def Changeicon(self, Img=None):
        if Img is None:
            self.img_path = filedialog.askopenfilename(
                title="Select an image",
                filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif"), ("All files", "*.*")]
            )
            if not self.img_path:
                return

            pil_image = Image.open(self.img_path)
            new_img = ctk.CTkImage(light_image=pil_image, size=(125, 125))
        else:
            if isinstance(Img, ctk.CTkImage):
                new_img = Img
            else:
                pil_image = Image.open(Img)
                new_img = ctk.CTkImage(light_image=pil_image, size=(125, 125))

        self.img.configure(image=new_img)
        self.img.image = new_img

    def createBtn(self):
        n = self.inp1.get()
        self.assets = self.inp2.get()
        desc = self.tbx3.get("1.0", "end")
        p = None
        self.dir = os.path.join(self.GlobalPath.replace('/', '\\'), self.inp1.get())
        if self.PathChanged:
            self.dir = os.path.join(self.NewPath.replace('/', '\\'), self.inp1.get())
            p = self.dir
        else:
            p = self.dir
        if self.assets == "" or self.assets == None:
            self.assets = "Assets"
        else:
            self.assets = self.inp2.get()
        img = self.img_path
        self.getCheckbox()
        created_files = [entry.get() for entry in self.CreatedFiles]
        Create_JData(n,desc,p,img,self.AddedFiles,created_files,self.assets)
        self.crearteFile()
    def getCheckbox(self):
        pass
    def Change_path(self):
        self.NewPath = ctk.filedialog.askdirectory(title= "Select Folder")
        self.path_inp1.configure(state="normal")
        self.path_inp1.delete("1.0", "end")
        self.path_inp1.insert("1.0", self.NewPath)
        self.PathChanged = True
        
    def crearteFile(self):
        try: 
            print(f"Window:{self.checkboxes}")
            if self.checkboxes == None or self.checkboxes == 0:
                ErrorWindow("Please select type")
            else:
                os.system(f"mkdir {self.dir}")
                print(dir)
                for file in self.CreatedFiles:
                    if file.get()== "":
                        return
                    os.system(f"echo. >{self.dir}\\{file.get()}")
                for file in self.AddedFiles:
                    if file == "":
                        return
                    os.system(f"copy {file} {self.dir}")
                    print(f"{file} {self.dir}")
                for file in self.Assets:
                    if file == "":
                        return
                    os.system(f"mkdir {self.dir}\\{self.assets}")
                    os.system(f"copy {file} {self.dir}\\{self.assets}")
                AlertWindow("Success", "Project created successfully!")
                import Apps
                Apps.Hub()
                self.window.destroy()
        except Exception as e:
            ErrorWindow(f"Error creando el proyecto: {e}")
        
import customtkinter as ctk
from PIL import Image
from tkinter import filedialog
import os
# Windows
class Window():
    def __init__(self,Size,title):
        ctk.set_default_color_theme("dark-blue")
        ctk.set_appearance_mode("dark")
        self.window = ctk.CTk()
        self.window.geometry(Size)
        self.container = ctk.CTkFrame(self.window)
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
                "Python_logo": ctk.CTkImage(light_image=Image.open(self.get_asset_path("Python_logo.png")), size=(250, 250)),
                "Web_Dev": ctk.CTkImage(light_image=Image.open(self.get_asset_path("Web_Dev.png")), size=(250, 250)),
                "C++_logo": ctk.CTkImage(light_image=Image.open(self.get_asset_path("C++_logo.png")), size=(250, 250)),
                "Code": ctk.CTkImage(light_image=Image.open(self.get_asset_path("Code.png")), size=(250, 250)),
                "3D": ctk.CTkImage(light_image=Image.open(self.get_asset_path("3D.png")), size=(250, 250)),                                     
                "imgSample": ctk.CTkImage(light_image=Image.open(self.get_asset_path("CyberLogo.png")), size=(125, 125))
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
    def __init__(self,error):
        super().__init__("600x200","Error")
        tx1 = ctk.CTkLabel(self.container, text=error, text_color="yellow", font=("Arial", 20, 'bold'))
        tx1.place(x=0,y=0)
        self.Run()

class PathWindow(Window):
    def __init__(self):
        super().__init__("600x200","Path")
        inp1 = ctk.CTkEntry(self.container, width=310, height=25, placeholder_text="Project path", fg_color="WHITE", text_color="BLACK")
        inp1.place(x=100, y=10)
        inp2 = ctk.CTkEntry(self.container, width=310, height=25, placeholder_text="Assets Path", fg_color="WHITE", text_color="BLACK")
        inp2.place(x=100, y=50)
        self.Run()

class ConfigWindow(Window):
    def __init__(self,title):
        super().__init__("600x600",title)
        self.canvas = ctk.CTkCanvas(self.container, width=745, height=745,bg="#333333",highlightthickness=0)
        self.canvas.place(x=0,y=0)    
        rect =self.canvas.create_rectangle(20, 5, 205, 180,outline="white", width=4)
        
        result = self.imgLoad()
        if isinstance(result, str):
            ErrorWindow(f"Error cargando imagenes {result}")
            print("esta mal")
        else:
            self.images = result
            self.img = ctk.CTkLabel(self.container, text="",image=self.images["imgSample"],bg_color="#333333")
            self.img.place(x=25,y=15)
        self.Files =[]
        self.Files2 =[]
        self.count = 0
        self.count2 = 0
        self.interface()
        self.ExternalContent()
        self.Run()
    def interface(self):
        inp1 = ctk.CTkEntry(self.container, width=310, height=25, placeholder_text="Project Name", fg_color="WHITE", text_color="BLACK",bg_color="#333333")
        btn = ctk.CTkButton(self.container, width=150, text="Create Files+",bg_color="#333333", command=self.AddFile)
        btn.place(x=10, y=180)
        btn2 = ctk.CTkButton(self.container, width=150, text="Add Files+",bg_color="#333333", command=self.OpenFile)
        btn2.place(x=170, y=180)
        btn3 = ctk.CTkButton(self.container, width=90, text="Change \nicon",bg_color="#333333", command=self.Changeicon)
        btn3.place(x=200, y=60)
        btn4 = ctk.CTkButton(self.container, width=120, height=40,text="Create!",fg_color="green")
        btn4.place(x=480, y=560)
        btn5 = ctk.CTkButton(self.container,width = 10,text=". . .",bg_color="#333333",command=PathWindow)
        btn5.place(x=570, y=0)
    def ExternalContent(self):
        pass
    def AddFile(self):
        y_position = 220 + (self.count * 40)
        inpF = ctk.CTkEntry(self.container, width=150, height=25, placeholder_text=f"New File {self.count + 1}", fg_color="WHITE", text_color="BLACK")
        inpF.place(x=10, y=y_position)
        self.Files.append(inpF)
        self.count += 1
    def OpenFile(self):
        file_path = filedialog.askopenfilename(title="Select file",filetypes=[("Todos los archivos", "*.*")])
        if file_path:
            y_pos = 220 + (self.count2 * 40)
            tx2 = ctk.CTkButton(self.container, text=file_path, text_color="white", font=("Arial", 12), command=lambda: self.RemoveFile(file_path, tx2))
            tx2.place(x=180, y=y_pos)
            self.Files2.append(file_path)
            self.count2 += 1
    def RemoveFile(self, file_path, button):
        if file_path in self.Files2:
            self.Files2.remove(file_path)
        button.destroy()
    def Changeicon(self):
        try:
            img_path = filedialog.askopenfilename(
                title="Select an image",
                filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif"), ("All files", "*.*")]
            )
            if img_path:
                new_img = ctk.CTkImage(light_image=Image.open(img_path), size=(125, 125))
                self.img.configure(image=new_img)
                self.img.image = new_img
                print(f"Ícono actualizado con éxito: {img_path}")
        except Exception as e:
            print(f"Error al cambiar el ícono: {e}")


class ElectronicConf(ConfigWindow):
    def __init__(self):
        super().__init__("Electronic conf")
    def ExternalContent(self):
        tx1 = ctk.CTkLabel(self.container, text="Type of project", text_color="white",bg_color="#333333", font=("Arial",20, 'bold'))
        tx1.place(x=400,y=20)
        cbox1 = ctk.CTkCheckBox(self.container, text="Display",bg_color="#333333")
        cbox1.place(x=400,y=70)
        cbox2 = ctk.CTkCheckBox(self.container, text="Devices",bg_color="#333333")
        cbox2.place(x=400,y=120)
        cbox3 = ctk.CTkCheckBox(self.container, text="Other",bg_color="#333333")
        cbox3.place(x=400,y=170)
class MechatronicConf(ConfigWindow):
    def __init__(self):
        super().__init__("Mechatronic conf")
    def ExternalContent(self):
        tx1 = ctk.CTkLabel(self.container, text="Enviroment", text_color="white",bg_color="#333333", font=("Arial",20, 'bold'))
        tx1.place(x=350,y=60)
        cbox1 = ctk.CTkCheckBox(self.container, text="C++",bg_color="#333333")
        cbox1.place(x=350,y=110)
        cbox2 = ctk.CTkCheckBox(self.container, text="Python",bg_color="#333333")
        cbox2.place(x=350,y=140)
        tx2 = ctk.CTkLabel(self.container, text="3D\n program", text_color="white",bg_color="#333333", font=("Arial",20, 'bold'))
        tx2.place(x=500,y=40)
        cbox1 = ctk.CTkCheckBox(self.container, text="Blender",bg_color="#333333")
        cbox1.place(x=500,y=110)
        cbox2 = ctk.CTkCheckBox(self.container, text="Fusion360",bg_color="#333333")
        cbox2.place(x=500,y=140)
class PythonConf(ConfigWindow):
    def __init__(self):
        super().__init__("Electronic conf")
    def ExternalContent(self):
        tx1 = ctk.CTkLabel(self.container, text="Type of project", text_color="white",bg_color="#333333", font=("Arial",20, 'bold'))
        tx1.place(x=400,y=20)
        cbox1 = ctk.CTkCheckBox(self.container, text="Hacking",bg_color="#333333")
        cbox1.place(x=400,y=70)
        cbox2 = ctk.CTkCheckBox(self.container, text="Games",bg_color="#333333")
        cbox2.place(x=400,y=120)
        cbox3 = ctk.CTkCheckBox(self.container, text="Apps",bg_color="#333333")
        cbox3.place(x=400,y=170)
        cbox4 = ctk.CTkCheckBox(self.container, text="Ai",bg_color="#333333")
        cbox4.place(x=500,y=70)
        cbox5 = ctk.CTkCheckBox(self.container, text="Math",bg_color="#333333")
        cbox5.place(x=500,y=120)
        cbox6 = ctk.CTkCheckBox(self.container, text="Other",bg_color="#333333")
        cbox6.place(x=500,y=170)
        
class C_Conf(ConfigWindow):
    def __init__(self):
        super().__init__("C++ conf")
    def ExternalContent(self):
        tx1 = ctk.CTkLabel(self.container, text="Type of project", text_color="white",bg_color="#333333", font=("Arial",20, 'bold'))
        tx1.place(x=400,y=20)
        cbox1 = ctk.CTkCheckBox(self.container, text="Game",bg_color="#333333")
        cbox1.place(x=400,y=70)
        cbox2 = ctk.CTkCheckBox(self.container, text="App",bg_color="#333333")
        cbox2.place(x=400,y=120)
        cbox3 = ctk.CTkCheckBox(self.container, text="Other",bg_color="#333333")
        cbox3.place(x=400,y=170)
        
class Web_Conf(ConfigWindow):
    def __init__(self):
        super().__init__("Web conf")
        def ExternalContent(self):
            pass
#Actions
class Create():
    def __init__(self):
        self.w1 = Window("1200x600","Cyber")
        result = self.w1.imgLoad()
        if isinstance(result, str):
            ErrorWindow(f"Error cargando imagenes {result}")
            print("esta mal")
        else:
            self.images = result
            self.MainWindow()
        self.w1.Run()

    def MainWindow(self):
        tx1 = ctk.CTkLabel(self.w1.container, text="   Welcome to Cyber!", text_color="white", font=("Arial", 60, 'bold'))
        tx1.place(x=350, y=80)
        tx2 = ctk.CTkLabel(self.w1.container, text="Select a project Template", text_color="white", font=("Arial",25))
        tx2.place(x=510, y=150)
        b1 = ctk.CTkButton(self.w1.container, width=200,height=200,image=self.images["img1"], text="",fg_color="#333333", command=lambda: self.B5())
        b1.place(x=60, y=250)
        b2 = ctk.CTkButton(self.w1.container, width=200,height=200,image=self.images["img2"], text="",fg_color="#333333", command=lambda: self.B1())
        b2.place(x=480, y=250)
        b3 = ctk.CTkButton(self.w1.container,width=200,height=200,image=self.images["img3"], text="",fg_color="#333333", command=lambda: self.ProgramingWindow())
        b3.place(x=870, y=250)
        ctk.CTkLabel(self.w1.container, text="   Mechatronic", text_color="white", font=("Arial", 35, 'bold')).place(x=60, y=520)
        ctk.CTkLabel(self.w1.container, text="     Electronic", text_color="white", font=("Arial", 35, 'bold')).place(x=480, y=520)
        ctk.CTkLabel(self.w1.container, text="  Programming", text_color="white", font=("Arial", 35, 'bold')).place(x=870, y=520)
    def ProgramingWindow(self):
        self.w1.Clear()
        tx4 = ctk.CTkLabel(self.w1.container, text="   Welcome to Cyber!", text_color="white", font=("Arial", 60, 'bold'))
        tx4.place(x=350, y=80)
        tx5 = ctk.CTkLabel(self.w1.container, text="Select a project Template", text_color="white", font=("Arial",25))
        tx5.place(x=510, y=150)
        b4 = ctk.CTkButton(self.w1.container, width=200,height=200,image=self.images["Python_logo"], text="",fg_color="#333333",command=lambda:self.B2())
        b4.place(x=60, y=250)
        b5 = ctk.CTkButton(self.w1.container, width=200,height=200,image=self.images["C++_logo"], text="",fg_color="#333333",command=lambda:self.B3())
        b5.place(x=480, y=250)
        b6 = ctk.CTkButton(self.w1.container,width=200,height=200,image=self.images["Web_Dev"], text="",fg_color="#333333",command=lambda:self.B4())
        b6.place(x=870, y=250)
        ctk.CTkLabel(self.w1.container, text="       Python", text_color="white", font=("Arial", 35, 'bold')).place(x=60, y=520)
        ctk.CTkLabel(self.w1.container, text="          C++", text_color="white", font=("Arial", 35, 'bold')).place(x=480, y=520)
        ctk.CTkLabel(self.w1.container, text="  Web\n Development", text_color="white", font=("Arial", 35, 'bold')).place(x=870, y=520)
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
        MechatronicConf()
        
Create()
#ElectronicConf() 
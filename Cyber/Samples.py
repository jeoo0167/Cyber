from Window import ConfigWindow
from JsonManager import Create_JData
import customtkinter as ctk
import tkinter as tk

class ElectronicConf(ConfigWindow):
    def __init__(self):
        super().__init__("Electronic conf")
        self.ExternalContent()
    def ExternalContent(self):
        Create_JData.Jdict.update({'Index':'Electronic Window'})
        self.Changeicon(self.get_asset_path("Img2.png"))
        self.img_path = self.get_asset_path("Img2.png")
        tx1 = ctk.CTkLabel(self.container,text="Type of project",text_color="white",bg_color="#333333",font=("Arial", 20, "bold"),)
        tx1.place(x=435, y=10)

        labels = ["Devices","Systems\nand\ncircuits", "Other"]
        positions = [(435, 50), (435, 100), (435, 150)]
        self.create_checkboxes(labels, positions, self.update_checkboxes)
    def getCheckbox(self):
        selected_index = None
        for i, var in enumerate(self.vars):
            if var.get() == 1: 
                selected_index = i
                break
        checkbox_values = ["Devices", "Systems\nand\ncircuits", "Other"]
        if selected_index is not None:
            print("true")
            selected_value = checkbox_values[selected_index]
            Create_JData.Jdict.update({'Type':f'type: {selected_value}'})
            print(selected_value)
        else:
            print("none")
            Create_JData.Jdict.update({'Type': None})

class MechatronicConf(ConfigWindow):
    def __init__(self):
        super().__init__("Mechatronic conf")

    def ExternalContent(self):
        Create_JData.Jdict.update({'Index':'Mechatronic Window'})
        self.Changeicon(self.get_asset_path("Img1.png"))
        self.img_path = self.get_asset_path("Img1.png")

class PythonConf(ConfigWindow):
    def __init__(self):
        super().__init__("Python conf")

    def ExternalContent(self):
        ctk.CTkLabel(self.container,text="Project Type",text_color="white",bg_color="#333333",font=("Arial", 20)).place(x=420,y=10)
        Create_JData.Jdict.update({'Index':'Programing Window:Python'})
        self.Changeicon(self.get_asset_path("Python_logo.png"))
        self.img_path = self.get_asset_path("Python_logo.png")
        self.labels=["Hacking","Games","apps","ai","Math","other"]
        self.positions =[(420,50),(420,100),(420,150),(525,50),(525,100),(525,150)]
        self.create_checkboxes(self.labels, self.positions, self.update_checkboxes)
    def getCheckbox(self):
        selected_index = None
        for i, var in enumerate(self.vars):
            if var.get() == 1: 
                selected_index = i
                break
        checkbox_values = ["Hacking","Games","apps","ai","Math","other"]
        
        if selected_index is not None:
            selected_value = checkbox_values[selected_index]
            Create_JData.Jdict.update({'Type': selected_value})
        else:
            Create_JData.Jdict.update({'Type': None})

class C_Conf(ConfigWindow):
    def __init__(self):
        super().__init__("C++ conf")

    def ExternalContent(self):
        ctk.CTkLabel(self.container,text="Project Type",text_color="white",bg_color="#333333",font=("Arial", 20)).place(x=420,y=10)
        Create_JData.Jdict.update({'Index':'Programing Window:C++'})
        self.Changeicon(self.get_asset_path("C++_logo.png"))
        self.img_path = self.get_asset_path("C++_logo.png")

        labels = ["Apps","Games", "Other"]
        positions = [(420,50),(420,100),(420,150)]
        self.create_checkboxes(labels, positions, self.update_checkboxes)
    def getCheckbox(self):
        selected_index = None
        for i, var in enumerate(self.vars):
            if var.get() == 1: 
                selected_index = i
                break

        checkbox_values = ["Apps","Games", "Other"]

        if selected_index is not None:
            selected_value = checkbox_values[selected_index]
            Create_JData.Jdict.update({'Type': selected_value})
        else:
            Create_JData.Jdict.update({'Type': None})

class JavaConf(ConfigWindow):
    def __init__(self):
        super().__init__("Java Conf")
    def ExternalContent(self):
        ctk.CTkLabel(self.container,text="Project Type",text_color="white",bg_color="#333333",font=("Arial", 20)).place(x=420,y=10)
        Create_JData.Jdict.update({'Index':'Programing Window:Java'})
        self.Changeicon(self.get_asset_path("Java_logo.png"))
        self.img_path = self.get_asset_path("Java_logo.png")

        labels = ["Apps","Minecraft \n Mods", "Games","Other"]
        positions = [(435, 50), (435, 100), (435, 150),(435,200)]
        self.create_checkboxes(labels, positions, self.update_checkboxes)
    def getCheckbox(self):
        selected_index = None
        for i, var in enumerate(self.vars):
            if var.get() == 1: 
                selected_index = i
                break

        checkbox_values = ["Apps","Minecraft Mods", "Games","Other"]

        if selected_index is not None:
            selected_value = checkbox_values[selected_index]
            Create_JData.Jdict.update({'Type': selected_value})
        else:
            Create_JData.Jdict.update({'Type': None})

class Web_Conf(ConfigWindow):
    def __init__(self):
        super().__init__("Web conf")
    def ExternalContent(self):
        Create_JData.Jdict.update({'Index':'Programing Window:Web'})
        self.Changeicon(self.get_asset_path("Web_Dev.png"))
        self.img_path = self.get_asset_path("Web_Dev.png")
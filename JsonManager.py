import json,os

class Create_JData:
    Jdict = {}
    #path = os.path.join(os.getenv('APPDATA'), '.cyber')
    path = "Jsons"
    def __init__(self, name,desc, P_path, I_path, F_path, F,assetName):
        self.name = name
        self.P_path = P_path
        self.I_path = I_path
        self.F_path = F_path
        self.F = F
        self.desc = desc
        self.path = Create_JData.path
        from datetime import datetime

        actualDate = datetime.now()

        date = actualDate.strftime("%d/%m/%Y")
        Create_JData.Jdict.update({
            "name": name,
            "Project_path": P_path,
            "Icon_path": I_path,
            "Files_path": F_path,
            "Files": F,
            "Asset Folder name":assetName,
            "date":date,
            "Description":self.desc,
        })
        self.output = json.dumps(Create_JData.Jdict, indent=4, separators=(",", ":"), sort_keys=True)

#        with open(f"{self.path}\\{self.name}.json","w") as file:
#           file.write(self.output)

        with open(f"jsons\\{self.name}.json","w") as file:
            file.write(self.output)

class JsonManager:
    def JWrite(file,data):
        with open(file, "w") as f:
            json.dump(data, f, indent=4)
    def JRead():
        data_list = []
        for Findfile in os.listdir(Create_JData.path):
            if Findfile.endswith(".json"):
                try:
                    with open(os.path.join(Create_JData.path, Findfile), "r") as f:
                        data = json.load(f)
                        data_list.append(data)
                except Exception as e:
                    from Window import ErrorWindow
                    ErrorWindow(f"Error reading {Findfile}: {e}")
        return data_list
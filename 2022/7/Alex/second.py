class File:
    def __init__(self,name:str,size:int,dir) -> None:
        self.name=name
        self.size=size
        self.parent:Dir=dir

    def get_size(self)->int:
        return self.size

class Dir:
    def __init__(self,name:str,dir) -> None:
        self.name=name
        self.files:dict[str,Dir|File]={}
        self.parent:Dir=dir

    def addChild(self,child:File):
        self.files[child.name]=child

    def getChild(self,child):

        return self.files.get(child,None)

    def get_dirs(self):
        res=[self]
        for entry in self.files.values():
            if type(entry)==Dir:
                res.extend(entry.get_dirs())
        return res

    def get_size(self):
        return sum(entry.get_size() for entry in self.files.values())


def main(input:str)->int:
    root=Dir("/",None)
    current=root

    for string in input.split("$")[1:]:
        lines=[line.strip() for line in string.splitlines()]
        splitcom=lines[0].split()
        output=lines[1:]

        match splitcom[0]:
            case "cd":
                match splitcom[1]:
                    case "/":
                        current=root
                    case "..":
                        current=current.parent
                    case other:
                        current=current.getChild(other)
            case "ls":
                for line in output:
                    info,name=line.split()
                    if info.isdigit():
                        current.addChild(File(name,int(info),current))
                    else:
                        current.addChild(Dir(name,current))

    min=30000000-(70000000-root.get_size())
    
    for dir in sorted([dir.get_size() for dir in root.get_dirs()]):
        if dir>min:
            return dir

if __name__=="__main__":
    with open("input.txt") as f:
        input=f.read()
    
    print(main(input))
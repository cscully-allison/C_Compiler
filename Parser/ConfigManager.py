import xml.etree.ElementTree as ET

class ConfigManager(object):
    def __init__(self, SourceFile):
        self.int = 0
        self.char = 0
        self.float = 0
        self.double = 0
        self.units = ""

        self.SetupConfig(SourceFile)

    def SetupConfig(self, SourceFile):
        tree = ET.parse(SourceFile)
        root = tree.getroot()

        for Child in root:
            if Child.tag == "DataTypes":
                self.units = Child.attrib["units"]
                for Type in Child:
                    setattr(self, Type.tag, Type.text)

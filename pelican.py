#import os
#import sys

##sys.path.append(os.path.join(os.path.dirnmae(__file__), 'utilities')
#sys.path.append(os.path.dirname(__file__))

#from pixelturtle import PixelTurtle

#my_turtle  pixelturtle.PixelTurtle()

import ScriptEnv

class HfssInterface:
    def __init__(self):
        ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
        oDesktop.RestoreWindow()
        self.project = oDesktop.GetActiveProject()
        self.design = self.project.SetActiveDesign("HFSSDesign1")

class HfssPixelArray:
    def __init__(self, o_design, pattern):
        self.design = o_design
        self.editor = None
        
        self.pattern = pattern
        self.width_name = "pixel_width"
        self.length_name = "pixel_length"
        self.height_name = "pixel_height"
        self.pixel_name = "pixel"
        
        self.pixel_width = 100
        self.pixel_width_unit = "um"
        self.pixel_length = 100
        self.pixel_length_unit = "um"
        self.pixel_height = 250
        self.pixel_height_unit = "um"
        
        self.axis = "Z"
        self.color = "(143 175 143)"
        
        self.add_variables()
        
    def draw(self):
        for (x, y) in self.pattern:
            self.draw_rectangle(x, y)
            
    def add_variables(self):
        self.design.ChangeProperty(
            ["NAME:AllTabs", ["NAME:LocalVariabelTab",
                ["NAME:PropServers", "LocalVariables"],
                ["NAME:NewProps", ["NAME:" + self.width_name, "PropTypes:=", "VariableProp", "UserDef:=", True, "Values:=", str(self.pixel_width) + self.pixel_width_unit]]
            ]])
        self.design.ChangeProperty(
            ["NAME:AllTabs", ["NAME:LocalVariabelTab",
                ["NAME:PropServers", "LocalVariables"],
                ["NAME:NewProps", ["NAME:" + self.length_name, "PropTypes:=", "VariableProp", "UserDef:=", True, "Values:=", str(self.pixel_length) + self.pixel_length_unit]]
            ]])
        self.design.ChangeProperty(
            ["NAME:AllTabs", ["NAME:LocalVariabelTab",
                ["NAME:PropServers", "LocalVariables"],
                ["NAME:NewProps", ["NAME:" + self.height_name, "PropTypes:=", "VariableProp", "UserDef:=", True, "Values:=", str(self.pixel_height) + self.pixel_height_unit]]
            ]])
            
    def draw_rectangle(self, x, y):
        self.editor = self.design.SetActiveEditor("3D Modeler")
        self.editor.CreateRectangle(
            [
                "NAME:RectangleParameters",
                "IsCovered:=", True,
                "XStart:=", str(x) + " * " + self.width_name,
                "YStart:=", str(y) + " * " + self.length_name,
                "ZStart:=", self.height_name,
                "Width:=", self.width_name,
                "Height:=", self.height_name,
                "WhichAxis:=", self.axis
            ],
            [
                "NAME:Attributes",
                "Name:=", self.pixel_name + "_" + str(x) + "_" + str(y),
                "Flags:=", "",
                "Color:=", self.color,
                "Transparency:=", 0,
                "PartCoorinateSystem:=", "Global",
                "UDMId:=", "",
                "MaterialValue:=", "\"vacuum\"",
                "SurfaceMaterialValue:=", "\"\"",
                "SolveInside:=", True,
                "ShellElement:=", False,
                "ShellElementThickness:=", "0mm",
                "ReferenceTemperature:=", "20cel",
                "IsMaterialEditable:=", True,
                "UseMaterialAppearance:=", False,
                "IsLightWeight:=", False
            ])

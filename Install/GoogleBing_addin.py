import arcpy
import pythonaddins
import webbrowser,math

class ToolClass2(object):
    """Implementation for GoogleBing_addin.tool (Tool)"""
    def __init__(self):
        self.enabled = True
        self.cursor = 3
        self.shape = None
    def onMouseDown(self, x, y, button, shift):
        pass
    def onMouseDownMap(self, x, y, button, shift):
        pass
    def onMouseUp(self, x, y, button, shift):
        pass
    def onMouseUpMap(self, x, y, button, shift):
        try:
            mxd = arcpy.mapping.MapDocument('CURRENT')
            df = arcpy.mapping.ListDataFrames(mxd)[0]
            sf,extent = df.spatialReference,df.extent
            pt = arcpy.PointGeometry(arcpy.Point(x,y),sf).projectAs(arcpy.SpatialReference(4326))
            ptwest = arcpy.PointGeometry(extent.lowerLeft,sf).projectAs(arcpy.SpatialReference(4326)).centroid.X
            pteast = arcpy.PointGeometry(extent.lowerRight, sf).projectAs(arcpy.SpatialReference(4326)).centroid.X
            angle = pteast-ptwest
            if angle<=0: angle+=360
            level = math.floor(math.log(1024*360/angle/256)/math.log(2))
            webbrowser.open('www.google.com/maps/@%f,%f,%dz'%(pt.centroid.Y,pt.centroid.X,level))
        except:pass
    def onMouseMove(self, x, y, button, shift):
        pass
    def onMouseMoveMap(self, x, y, button, shift):
        pass
    def onDblClick(self):
        pass
    def onKeyDown(self, keycode, shift):
        pass
    def onKeyUp(self, keycode, shift):
        pass
    def deactivate(self):
        pass
    def onCircle(self, circle_geometry):
        pass
    def onLine(self, line_geometry):
        pass
    def onRectangle(self, rectangle_geometry):
        pass

class ToolClass4(object):
    """Implementation for GoogleBing_addin.tool_1 (Tool)"""
    def __init__(self):
        self.enabled = True
        self.shape = "NONE" # Can set to "Line", "Circle" or "Rectangle" for interactive shape drawing and to activate the onLine/Polygon/Circle event sinks.
    def onMouseDown(self, x, y, button, shift):
        pass
    def onMouseDownMap(self, x, y, button, shift):
        pass
    def onMouseUp(self, x, y, button, shift):
        pass
    def onMouseUpMap(self, x, y, button, shift):
        try:
            mxd = arcpy.mapping.MapDocument('CURRENT')
            df = arcpy.mapping.ListDataFrames(mxd)[0]
            sf = df.spatialReference
            pt = arcpy.PointGeometry(arcpy.Point(x, y), sf).projectAs(arcpy.SpatialReference(4326))
            webbrowser.open('www.google.com/maps/@%f,%f,15z/data=!3m1!1e3!5m1!1e4' % (pt.centroid.Y, pt.centroid.X))
        except:
            pass
    def onMouseMove(self, x, y, button, shift):
        pass
    def onMouseMoveMap(self, x, y, button, shift):
        pass
    def onDblClick(self):
        pass
    def onKeyDown(self, keycode, shift):
        pass
    def onKeyUp(self, keycode, shift):
        pass
    def deactivate(self):
        pass
    def onCircle(self, circle_geometry):
        pass
    def onLine(self, line_geometry):
        pass
    def onRectangle(self, rectangle_geometry):
        pass
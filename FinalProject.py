import os
import sys
import wave
import math
import struct
import random
import argparse
from itertools import *
import wx
import random
from array import *

class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        self.dirname=''

        # A "-1" in the size parameter instructs wxWidgets to use the default size.
        # In this case, we select 200px width and the default height.
        wx.Frame.__init__(self, parent, title=title, size=(200,-1))
        self.CreateStatusBar() # A Statusbar in the bottom of the window

        # Setting up the menu.
        filemenu= wx.Menu()
        menuClear = filemenu.Append(wx.ID_CLEAR, "&Clear", "Clear the screen")
        menuOpen = filemenu.Append(wx.ID_OPEN, "&Open"," Open a file to edit")
        menuSave = filemenu.Append(wx.ID_SAVE, "&Save"," Save the Image")
        menuAbout= filemenu.Append(wx.ID_ABOUT, "&About"," Information about this program")
        menuExit = filemenu.Append(wx.ID_EXIT,"E&xit"," Terminate the program")

        # Creating the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&File") # Adding the "filemenu" to the MenuBar
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.

        # Events.
        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnSave, menuSave)
        self.Bind(wx.EVT_MENU, self.OnClear, menuClear)

        self.sizer2 = wx.BoxSizer(wx.HORIZONTAL)
        self.buttons = []
        for i in range(0, 12):
            self.buttons.append(wx.Button(self, -1, "Button &"+str(i)))
            self.sizer2.Add(self.buttons[i], 1, wx.EXPAND)

        self.buttons[0].SetLabel("Load")
        self.buttons[0].Bind(wx.EVT_BUTTON, self.ButtonClick)
        self.buttons[1].SetLabel("Blur")
        self.buttons[1].Bind(wx.EVT_BUTTON, self.ButtonClick2)
        self.buttons[2].SetLabel("Glass")
        self.buttons[2].Bind(wx.EVT_BUTTON, self.ButtonClick3)
        self.buttons[3].SetLabel("Inverse")
        self.buttons[3].Bind(wx.EVT_BUTTON, self.ButtonClick4)
        self.buttons[4].SetLabel("Solarize")
        self.buttons[4].Bind(wx.EVT_BUTTON, self.ButtonClick5)
        self.buttons[5].SetLabel("Posterize")
        self.buttons[5].Bind(wx.EVT_BUTTON, self.ButtonClick6)
        self.buttons[6].SetLabel("GreyScale")
        self.buttons[6].Bind(wx.EVT_BUTTON, self.ButtonClick7)
        self.buttons[7].SetLabel("Combination")
        self.buttons[7].Bind(wx.EVT_BUTTON, self.ButtonClick8)
        
        
        # Use some sizers to see layout options
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.sizer2, 0, wx.EXPAND)

        #Layout sizers
        self.SetSizer(self.sizer)
        self.SetAutoLayout(1)
        self.sizer.Fit(self)
        self.Show()
        
    
    def ButtonClick(self, e):
        png = wx.Image("C:\\Images\\leaf.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        wx.StaticBitmap(self, -1, png, (0, 0), (png.GetWidth(), png.GetHeight()))
    
                
    def ButtonClick2(self, e):
        png = wx.Image("C:\\Images\\Leaf.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.myBlur(png)
        wx.StaticBitmap(self, -1, png, (0, 0), (png.GetWidth(), png.GetHeight()))
    

    def ButtonClick3(self,e):
        png = wx.Image("C:\\Images\\leaf.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.glassfilter(png)
        wx.StaticBitmap(self, -1, png, (0, 0), (png.GetWidth(), png.GetHeight()))

    def ButtonClick4(self,e):
        png = wx.Image("C:\\Images\\leaf.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.inversefilter(png)
        wx.StaticBitmap(self, -1, png, (0, 0), (png.GetWidth(), png.GetHeight()))
    
    def ButtonClick5(self,e):
        png = wx.Image("C:\\Images\\leaf.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.solarizefilter(png)
        wx.StaticBitmap(self, -1, png, (0, 0), (png.GetWidth(), png.GetHeight()))
       
    def ButtonClick6(self,e):
        png = wx.Image("C:\\Images\\leaf.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.posterizefilter(png)
        wx.StaticBitmap(self, -1, png, (0, 0), (png.GetWidth(), png.GetHeight()))
        
    def ButtonClick7(self,e):
        png = wx.Image("C:\\Images\\leaf.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.greyscalefilter(png)
        wx.StaticBitmap(self, -1, png, (0, 0), (png.GetWidth(), png.GetHeight()))   
        
    def ButtonClick8(self,e):
        png = wx.Image("C:\\Images\\leaf.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.greyscalefilter(png)
        self.posterizefilter(png)
        self.warholefilter(png)
        wx.StaticBitmap(self, -1, png, (0, 0), (png.GetWidth(), png.GetHeight())) 

    
    def OnAbout(self,e):
        # Create a message dialog box
        dlg = wx.MessageDialog(self, " A sample editor \n in wxPython", "About Sample Editor", wx.OK)
        dlg.ShowModal() # Shows it
        dlg.Destroy() # finally destroy it when finished.
        
    def OnSave(self,e,):
        #img=bmpicture.ConvertToImage()
        #img.SaveFile("test2.png", wx.BITMAP_TYPE_PNG)
        self.Close(True)
        

    def OnExit(self,e):
        self.Close(True)  # Close the frame.

    def OnOpen(self,e):
        """ Open a file"""
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), 'r')
            self.control.SetValue(f.read())
            f.close()
        dlg.Destroy()
        
    def OnClear(self,e):
        dc = wx.MemoryDC()
        dc.Clear(self)
        
    def warholefilter(self,bmpicture):
        interval_values=array('i')
        interval_count=32
        group_size=256/interval_count
        for i in range(0,interval_count-1):
            interval_values.append(group_size*i)
        width= wx.Bitmap.GetWidth(bmpicture)
        height= wx.Bitmap.GetHeight(bmpicture)
        dc = wx.MemoryDC()
        dc.SelectObject(bmpicture)
        hue=wx.Colour()
        for y in range(1, height-1):
            for x in range(1, width-1):
                hue=wx.DC.GetPixel(dc,x,y)
                newred2=wx.Colour.Red(hue)
                newblue2=wx.Colour.Blue(hue)
                newgreen2=wx.Colour.Green(hue)
                sums= newred2 + newblue2+ newgreen2
                averages=sums/3
                newaverages=int(256/averages)
                if newaverages<interval_count:
                    
                newred=wx.Colour.Red(hue)
                hue.Red=interval_values[int(newred/group_size)-1]
                
                
                
                newblue=wx.Colour.Blue(hue)
                hue.Blue=interval_values[int(newblue/group_size)-1]

                newgreen=wx.Colour.Green(hue)
                hue.Green=interval_values[int(newgreen/group_size)-1]
                
                newcolor=wx.Colour(hue.Red,hue.Blue,hue.Green,255)
                mypen=wx.Pen(newcolor)
                wx.Pen.SetColour(mypen,newcolor)
                wx.DC.SetPen(dc,mypen)
                wx.DC.DrawPoint(dc,x,y)
        dc.SelectObject(wx.NullBitmap)        
        return bmpicture    
    
    def greyscalefilter( self, bmpicture):
        width= wx.Bitmap.GetWidth(bmpicture)
        height= wx.Bitmap.GetHeight(bmpicture)
        dc = wx.MemoryDC()
        dc.SelectObject(bmpicture)
        hue=wx.Colour()
        oldP=wx.Colour()
        for y in range(1, height-1):
            for x in range(1, width-1):
                hue=wx.DC.GetPixel(dc,x,y)
                newred=wx.Colour.Red(hue)
                newblue=wx.Colour.Blue(hue)
                newgreen=wx.Colour.Green(hue)
                sums= newred + newblue+ newgreen
                averages=sums/3
                oldP=wx.Colour(averages,averages,averages,255)
                mypen=wx.Pen(oldP)
                wx.Pen.SetColour(mypen,oldP)
                wx.DC.SetPen(dc,mypen)
                wx.DC.DrawPoint(dc,x,y)
        dc.SelectObject(wx.NullBitmap)
        return bmpicture
        
    def posterizefilter(self,bmpicture):
        interval_values=array('i')
        interval_count=32
        group_size=256/interval_count
        for i in range(0,interval_count-1):
            interval_values.append(group_size*i)
        width= wx.Bitmap.GetWidth(bmpicture)
        height= wx.Bitmap.GetHeight(bmpicture)
        dc = wx.MemoryDC()
        dc.SelectObject(bmpicture)
        hue=wx.Colour()
        for y in range(1, height-1):
            for x in range(1, width-1):
                hue=wx.DC.GetPixel(dc,x,y)

                newred=wx.Colour.Red(hue)
                hue.Red=interval_values[int(newred/group_size)-1]
                
                newblue=wx.Colour.Blue(hue)
                hue.Blue=interval_values[int(newblue/group_size)-1]

                newgreen=wx.Colour.Green(hue)
                hue.Green=interval_values[int(newgreen/group_size)-1]
                
                newcolor=wx.Colour(hue.Red,hue.Blue,hue.Green,255)
                mypen=wx.Pen(newcolor)
                wx.Pen.SetColour(mypen,newcolor)
                wx.DC.SetPen(dc,mypen)
                wx.DC.DrawPoint(dc,x,y)
        dc.SelectObject(wx.NullBitmap)        
        return bmpicture
                
                       
    def solarizefilter(self, bmpicture):
        width= wx.Bitmap.GetWidth(bmpicture)
        height= wx.Bitmap.GetHeight(bmpicture)
        dc = wx.MemoryDC()
        dc.SelectObject(bmpicture)
        hue=wx.Colour()
        oldP=wx.Colour()
        Threshold = 150
        for y in range(1, height-1):
            for x in range(1, width-1):
                hue=wx.DC.GetPixel(dc,x,y)
                newred=wx.Colour.Red(hue)
                newblue=wx.Colour.Blue(hue)
                newgreen=wx.Colour.Green(hue)
                sums= newred + newblue+ newgreen
                averages=sums/3
                if averages<Threshold:
                    newred=255-wx.Colour.Red(hue)
                    newblue=255-wx.Colour.Blue(hue)
                    newgreen=255-wx.Colour.Green(hue)
                    oldP=wx.Colour(newred,newgreen,newblue,255)
                else:                    
                    oldP=wx.Colour(averages,255)
                mypen=wx.Pen(oldP)
                wx.Pen.SetColour(mypen,oldP)
                wx.DC.SetPen(dc,mypen)
                wx.DC.DrawPoint(dc,x,y)
        dc.SelectObject(wx.NullBitmap)        
        return bmpicture
        
    def inversefilter(self, bmpicture):
        width= wx.Bitmap.GetWidth(bmpicture)
        height= wx.Bitmap.GetHeight(bmpicture)
        dc = wx.MemoryDC()
        dc.SelectObject(bmpicture)
        """Goes pixel by Pixel"""
        hue=wx.Colour()
        oldP=wx.Colour()
        for y in range(1, height-1):
            for x in range(1, width-1):
                hue=wx.DC.GetPixel(dc,x,y)
                newred=255-wx.Colour.Red(hue)
                newblue=255-wx.Colour.Blue(hue)
                newgreen=255-wx.Colour.Green(hue)
                oldP=wx.Colour(newred,newgreen,newblue,255)
                mypen=wx.Pen(oldP)
                wx.Pen.SetColour(mypen,oldP)
                wx.DC.SetPen(dc,mypen)
                wx.DC.DrawPoint(dc,x,y)
        dc.SelectObject(wx.NullBitmap)        
        return bmpicture
         
    def glassfilter(self, bmpicture):
        width= wx.Bitmap.GetWidth(bmpicture)
        height= wx.Bitmap.GetHeight(bmpicture)
        Distance=5
        dc = wx.MemoryDC()
        dc.SelectObject(bmpicture)
        """Goes pixel by Pixel"""
        for y in range(1, height-1):
            for x in range(1, width-1):
                xrand=x+random.random()*Distance*2-Distance
                yrand=y+random.random()*Distance*2-Distance
                oldP=wx.DC.GetPixel(dc,xrand,yrand)
                mypen=wx.Pen(oldP)
                wx.Pen.SetColour(mypen,oldP)
                wx.DC.SetPen(dc,mypen)
                wx.DC.DrawPoint(dc,x,y)
        dc.SelectObject(wx.NullBitmap)        
        return bmpicture
                 
    def tripleSum2(self,(r1, g1, b1), (r2,g2,b2)):
        return(r1+r2,g1+g2,b1+b2)

    
    def myBlur(self,bmpicture):
        """Builds and returns a new image which is a blurred copy of the argument image"""    
        width= wx.Bitmap.GetWidth(bmpicture)
        height= wx.Bitmap.GetHeight(bmpicture) 
        dc = wx.MemoryDC()
        dc.SelectObject(bmpicture)
        """Goes pixel by Pixel"""
        for y in range(1, height-1):
            for x in range(1, width-1):
                oldP=wx.DC.GetPixel(dc,x,y)
                left=wx.DC.GetPixel(dc,x-1,y)
                right=wx.DC.GetPixel(dc,x+1, y)
                top=wx.DC.GetPixel(dc,x,y-1)
                bottom=wx.DC.GetPixel(dc,x,y+1)
                sums=reduce(self.tripleSum2,[oldP, left, right, top, bottom])
                averages=tuple(map(lambda x: x/5, sums))
                mypen=wx.Pen(averages)
                wx.Pen.SetColour(mypen,averages)
                wx.DC.SetPen(dc,mypen)
                wx.DC.DrawPoint(dc,x,y)
        dc.SelectObject(wx.NullBitmap)        
        return bmpicture
   
  
app = wx.App(False)
frame = MainWindow(None, "image and sound")
app.MainLoop()
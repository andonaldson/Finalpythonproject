import os
import wx
import random

class MainWindow(wx.Frame):

    def __init__(self, parent, title):
        self.dirname=''

        # A "-1" in the size parameter instructs wxWidgets to use the default size.
        # In this case, we select 200px width and the default height.
        wx.Frame.__init__(self, parent, title=title, size=(200,-1))
        self.CreateStatusBar() # A Statusbar in the bottom of the window

        # Setting up the menu.
        filemenu= wx.Menu()
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

        self.sizer2 = wx.BoxSizer(wx.HORIZONTAL)
        self.buttons = []
        for i in range(0, 11):
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

        # Use some sizers to see layout options
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.sizer2, 0, wx.EXPAND)

        #Layout sizers
        self.SetSizer(self.sizer)
        self.SetAutoLayout(1)
        self.sizer.Fit(self)
        self.Show()

    def ButtonClick(self,e):
        png = wx.Image("C:\\Images\\leaf.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        wx.StaticBitmap(self, -1, png, (0, 0), (png.GetWidth(), png.GetHeight()))
                      
    def ButtonClick2(self,e):
        png = wx.Image("C:\\Images\\leaf.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
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
       



    def OnAbout(self,e):
        # Create a message dialog box
        dlg = wx.MessageDialog(self, " A sample editor \n in wxPython", "About Sample Editor", wx.OK)
        dlg.ShowModal() # Shows it
        dlg.Destroy() # finally destroy it when finished.
        
    def OnSave(self,e):
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
        
    def solarizefilter(self, bmpicture):
    	width= wx.Bitmap.GetWidth(bmpicture)
        height= wx.Bitmap.GetHeight(bmpicture)
        size = width,height
        dc = wx.MemoryDC()
        dc.SelectObject(bmpicture)
        hue=wx.Colour()
        oldP=wx.Colour()
        Threshold = 5 
        for y in range(1, height-1):
            for x in range(1, width-1):
            	hue=wx.DC.GetPixel(dc,x,y)
            	newred=wx.Colour.Red(hue)
            	newblue=wx.Colour.Blue(hue)
            	newgreen=wx.Colour.Green(hue)
            	oldP=wx.Colour(newred,newgreen,newblue,255)
                mypen=wx.Pen(oldP)
                wx.Pen.SetColour(mypen,oldP)
                wx.DC.SetPen(dc,mypen)
                wx.DC.DrawPoint(dc,x,y)
        
    def inversefilter(self, bmpicture):
    	width= wx.Bitmap.GetWidth(bmpicture)
        height= wx.Bitmap.GetHeight(bmpicture)
        size = width,height
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
         
    def glassfilter(self, bmpicture):
    	width= wx.Bitmap.GetWidth(bmpicture)
        height= wx.Bitmap.GetHeight(bmpicture)
        size = width,height
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
                 
    def tripleSum2(self,(r1, g1, b1), (r2,g2,b2)):
        return(r1+r2,g1+g2,b1+b2)
	
    def myBlur(self, bmpicture):
        """Builds and returns a new image which is a blurred copy of the argument image"""		
        width= wx.Bitmap.GetWidth(bmpicture)
        height= wx.Bitmap.GetHeight(bmpicture) 
        size = width,height
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
frame = MainWindow(None, "Sample editor")
app.MainLoop()

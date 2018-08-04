try:
    from OpenGL.GL import *
except ImportError:
    raise ImportError, "Required dependency OpenGL not present"

import wx
try:
    from wx import glcanvas
except ImportError:
    raise ImportError, "Required dependency wx.glcanvas not present"

class GLFrame(wx.Frame):
    def __init__(self, parent, id, title, pos=wx.DefaultPosition,
                 size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE,
                 name='glframe'):
        style = wx.DEFAULT_FRAME_STYLE | wx.NO_FULL_REPAINT_ON_RESIZE

        super(GLFrame, self).__init__(parent, id, title, pos, size, style, name)

        self.GLinitialised = False
        attribList = (glcanvas.WX_GL_RGBA, glcanvas.WX_GL_DOUBLEBUFFER, glcanvas.WX_GL_DEPTH_SIZE, 24)

        self.canvas = glcanvas.GLCanvas(self, attribList=attribList)

        self.canvas.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        self.canvas.Bind(wx.EVT_SIZE, self.OnSize)
        self.canvas.Bind(wx.EVT_PAINT, self.OnPaint)

    def GetGLExtents(self):
        return self.canvas.GetClientSize()

    def SwapBuffer(self):
        self.canvas.SwapBuffers()

    def OnEraseBackground(self, event):
        pass

    def OnSize(self, event):
        if self.canvas.GetContext():
            self.Show()
            self.canvas.SetCurrent()
            size = self.GetGLExtents()
            self.OnReshape(size.width, size.height)
            self.canvas.Refresh(False)
        event.Skip()

    def OnPaint(self, event):
        self.canvas.SetCurrent()
        if not self.GLinitialised:
            self.OnInitGL()
            elf.GLinitialised = True

        self.OnDraw()
        event.Skip()

    def OnInitGL(self):
        glClearColor(1, 1, 1, 1)

    def OnReshape(self, width, height):
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-0.5, 0.5, -0.5, 0.5, -1, 1)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def OnDraw(self, *args, **kwargs):
        glClear(GL_COLOR_BUFFER_BIT)

        glBegin(GL_TRIANGLES)
        glColor(0, 0, 0)
        glVertex(-.25, -.25)
        glVertex(.25, -.25)
        glVertex(0, .25)
        glEnd()

        self.SwapBuffers()

class MSEApp(wx.Frame):

    def __init__(self, parent, title):
        super(MSEApp, self).__init__(parent, title=title, size=(1024, 600))
        self.Initialise()

    def Initialise(self):
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        fileMenu.Append(wx.ID_NEW, '&New')
        fileMenu.Append(wx.ID_OPEN, '&Open...')
        fileMenu.Append(wx.ID_SAVE, '&Save')
        fileMenu.Append(wx.ID_SAVEAS, 'Save &As...')
        fileMenu.AppendSeparator()
        qmi = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)

        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetStatusText('Ready')

        self.Bind(wx.EVT_MENU, self.OnQuit, qmi)

    def OnQuit(self, e):
        self.Close()

def main():
    app = wx.App()
    mse = MSEApp(None, title='Model Scene Editor')
    mse.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
    

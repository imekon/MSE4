import wx

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
    

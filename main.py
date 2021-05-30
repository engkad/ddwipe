

import gi

gi.require_version('Gtk','3.0')

from gi.repository import Gtk as gtk




class Main:
    def __init__(self):
        gladeFile = 'ui.glade'
        self.builder = gtk.Builder()
        self.builder.add_from_file(gladeFile)

        button = self.builder.get_object('button')
        button.connect('clicked', self.printText)

        window = self.builder.get_object('main')
        window.connect('delete-event', gtk.main_quit)
        window.show()

        startWipe = self.builder.get_object('startWipe')
        startWipe.connect('clicked', self.startWipe)

        launchAbout = self.builder.get_object('aboutButton')
        launchAbout.connect('clicked', self.launchAbout)

        warning = self.builder.get_object('warning')
        warning.show()

    def launchAbout(self,widget):
        aboutwindow = self.builder.get_object('aboutdialog1')
        aboutwindow.run()
        aboutwindow.hide()


    def printText(self,widget):
        # gets the path specified
        selectDrive = self.builder.get_object('driveEntry')
        drivePath = selectDrive.get_text()
        print(drivePath)

    def startWipe(self,widget):
        selectDrive = self.builder.get_object('driveEntry')
        drivePath = selectDrive.get_text()

        blockSize = self.builder.get_object('blockSize').get_text()

        command = 'dd if=/dev/zero of='+str(drivePath)+' bs='+str(blockSize)+' status=progress'

        print(command)









if __name__ == '__main__':
    main = Main()
    gtk.main()


import gi
import subprocess
import time
import sys
import signal

# from ddwipe import *

gi.require_version('Gtk','3.0')

from subprocess import Popen, PIPE
from gi.repository import Gtk as gtk

# tdd.wipe(1,2,3)


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

        stopWipe = self.builder.get_object('stopWipe')
        stopWipe.connect('clicked', self.stopWipe)

        launchAbout = self.builder.get_object('aboutButton')
        launchAbout.connect('clicked', self.launchAbout)

        warning = self.builder.get_object('warning')
        warning.show()

        launchOptions = self.builder.get_object('optionsButton')
        launchOptions.connect('clicked', self.launchOptions)

    def launchAbout(self,widget):
        aboutwindow = self.builder.get_object('aboutdialog1')
        aboutwindow.run()
        aboutwindow.hide()

    def launchOptions(self,widget):
        optionsWindow = self.builder.get_object('optionsDialog')
        optionsWindow.run()
        optionsWindow.hide()

    def printText(self,widget):
        # gets the path specified
        selectDrive = self.builder.get_object('driveEntry')
        drivePath = selectDrive.get_text()
        print(drivePath)

    def checkOutput(self):
        viewer = self.builder.get_object('outputView')

        while True:
            output = self.process.stdout.readline()
            if self.process.poll() is not None:
                break
            if output:
                print(output.strip())

        rc = self.process.poll()

    def startWipe(self,widget):
        selectDrive = self.builder.get_object('driveEntry')
        drivePath = selectDrive.get_text()

        inputEntry = self.builder.get_object('inputEntry')
        inputPath = inputEntry.get_text()

        blockSize = self.builder.get_object('blockSize').get_text()

        command = 'dd if=/dev/zero of='+str(drivePath)+' bs='+str(blockSize)+' status=progress'

        print(command)


        dd = ['dd', 'if='+inputPath, 'of='+drivePath,'bs='+blockSize,'status=progress']

        self.process = subprocess.Popen(dd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

        self.checkOutput()

    

        # while True:
            # # out = subprocess.check_output(dd).decode(sys.stdout.encoding)
            # out, err = process.communicate()
            # ddOut = self.builder.get_object('ddOut')
            # if out == None:
                # pass
            # else:
                # outStr = str(out)
                # ddOut.set_label('outStr')
                # print(outStr)

            # poll = process.poll()
            # if poll is None:
                # # process is alive
                # pass
            # else:
                # # process has ended
                # break
    def stopWipe(self,widget):
        self.process.kill()

    














if __name__ == '__main__':
    main = Main()
    gtk.main()


import gi
import subprocess
import time
import sys
import signal

from subprocess import Popen, PIPE
from gi.repository import Gtk as gtk

gi.require_version('Gtk','3.0')


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


        dd = ['dd', 'if=/tmp/test.txt', 'of='+drivePath,'bs='+blockSize,'status=progress']
        # while dd.poll() is None:
            # time.sleep(.3)
            # dd.send_signal(signal.SIGUSR1)
            # while 1:
                # l = dd.stderr.readline()
                # if 'records in' in l:
                    # print l[:l.index('+')], 'records',
                # if 'bytes' in l:
                    # print l.strip(), '\r',
                    # break
        # print dd.stderr.read(),

        # process = subprocess.Popen(dd, stderr=subprocess.STDOUT)

        # line = ''
        # while True:
        #     out = process.stderr.read(1)
        #     if out == '' and process.poll() != None:
        #         break
        #     if out != '':
        #         s = out.decode("utf-8")
        #         if s == '\r':
        #             print(line)
        #             ddOut = self.builder.get_object('ddOut')
        #             ddOut.set_text(line)
        #             line = ''
        #         else:
        #             line = line + s

        while True:
            out = subprocess.check_output(dd).decode(sys.stdout.encoding)
            ddOut = self.builder.get_object('ddOut')
            ddOut.set_label(out)
            print(out)

            poll = out.poll()
            if poll is None:
                # process is alive
                pass
            else:
                # process has ended
                break














if __name__ == '__main__':
    main = Main()
    gtk.main()
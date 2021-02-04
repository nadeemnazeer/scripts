# Notifier example to watch what is acccessed from a directory
#Usage python watch.py <path>
#
# See: http://github.com/seb-m/pyinotify/wiki/Tutorial
#
import pyinotify
import sys
path = sys.argv[1]
wm = pyinotify.WatchManager()  # Watch Manager
mask = pyinotify.IN_ACCESS | pyinotify.IN_CREATE  # watched events

class EventHandler(pyinotify.ProcessEvent):
    def process_IN_CREATE(self, event):
        print( "Creating:", event.pathname)

    def process_IN_ACCESS(self, event):
        print("Accessing:", event.pathname)

handler = EventHandler()
notifier = pyinotify.Notifier(wm, handler)
wdd = wm.add_watch(path, mask, rec=True)

notifier.loop()

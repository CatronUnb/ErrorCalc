import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

class Display(Gtk.Entry):
    def __init__(self):
        Gtk.Entry.__init__(self)
        self.connect('key-release-event', self.on_key_release)
        self.set_editable(False)

    def on_key_release(self, widget, event):
        acceptable_entry = [x for x in range(48, 58)] + [x for x in range(65456, 65466)]
        if event.keyval in acceptable_entry:
            if event.keyval in range(65456, 65466):
                event.keyval -= 65408
            curr_txt = widget.get_text()
            curr_txt += chr(event.keyval)
            widget.set_text(curr_txt)
        
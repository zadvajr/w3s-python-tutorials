#print to printer
import tempfile
import win32api
import win32print

filename = temfile.mktemp(".txt")
win32api.ShellExecute (
    0,
    "print",
    filename,
    '/d:"%s"' % win32print.GetDefaultPrinter (),
    ".",
)
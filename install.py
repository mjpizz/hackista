import editor, requests

print "* Downloading pipista"
pipista_code = requests.get("https://raw.githubusercontent.com/mjpizz/hackista/master/pipista.py").text

print "* Installing pipista"
editor.make_new_file("pipista", pipista_code)
editor.reload_files()

try:
    print "* Verifying pipista installation"
    import pipista
    print "* Successfully installed pipista"
except ImportError:
    print "* Error: failed to instal pipista"
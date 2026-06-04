Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s='     hello   world   '
s
'     hello   world   '
s.strip()
'hello   world'
s.lstrip()
'hello   world   '
s.rstrip()
'     hello   world'
s='strings.py'
s
'strings.py'
s.startswith('str')
True
s.endswith('py')
True
s.endswith('js')
False
'stfyui'.isalpha()
True
'ed3'.isalnum()
True
'python'.islower()
True
'Python'.islower()
False
'honey@1223.isalpha()
SyntaxError: unterminated string literal (detected at line 1)
'honey@1223'.isalpha()
False
'njdudbjskci'.isalnum()
True
'Abggynjcjicjd'.isupper()
False
'bnshdysns'.isupper()
False
' '.isspace()
True
' python    '.isspace()
False
'py prg lan'.istitle()
False
'Py prg lan'.istitle()
False
'Py Prg Lan'.istitle()
True
'py_python'.isidentifier()
True
'py@123'.isidentifier()
False

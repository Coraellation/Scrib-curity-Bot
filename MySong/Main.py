__author__ = 'George'

import Note
from myro import *
init("COM3")

tempo = 2
qq = 0.25
q = 0.2
h = 1

#bar 1
beep(q, Note.e[6], Note.c[4])
beep(q, Note.e[6], Note.g[4])
beep(q, Note.f[6], Note.c[5])
beep(q, Note.g[6], Note.e[5])
beep(q, Note.c[6])
beep(q, Note.c[5])
beep(q, Note.g[4])
beep(q, Note.c[4])

#bar 2
beep(q, Note.b[5], Note.g[3])
beep(q, Note.b[5], Note.c[4])
beep(q, Note.c[6], Note.g[4])
beep(q, Note.d[6], Note.b[4])
beep(q, Note.g[5])
beep(q, Note.g[4])
beep(q, Note.c[4])
beep(q, Note.g[3])

#bar 3
beep(q, Note.e[6], Note.a[3])
beep(q, Note.e[6], Note.e[4])
beep(q, Note.a[6], Note.a[4])
beep(q, Note.c[7], Note.c[5])
beep(q, Note.b[6])
beep(q, Note.a[6], Note.a[4])
beep(q, Note.g[6], Note.e[4])
beep(q, Note.e[6], Note.a[3])

#bar 4
beep(q, Note.g[6], Note.e[4])
beep(q, Note.b[4])
beep(q, Note.e[5])
beep(q, Note.g[5])
beep(q, Note.c[1])
beep(q, Note.e[5])
beep(q, Note.e[5], Note.b[4])
beep(q, Note.g[6], Note.e[4])


speak(song, 0)
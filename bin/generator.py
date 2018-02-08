#!/usr/bin/env python

import sys
import os
from dateutil.relativedelta import relativedelta
import datetime
from dateutil.parser import parse
import re
from datetime import datetime

if (len(sys.argv) != 4):
    sys.stderr.write("Modo de uso %s <archivo> <iteraciones> <salida>\n" % __file__)
    sys.exit(1)

if (not os.path.isfile(sys.argv[1])):
    sys.stderr.write("%s: no es un archivo valido\n" % sys.argv[1])
    sys.exit(2)

if (not sys.argv[2].isdigit()):
    sys.stderr.write("%s: no es numerico\n" % sys.argv[2])
    sys.exit(2)
    
count = int(sys.argv[2])
filename = sys.argv[1]
out = open(sys.argv[3], 'w')

date_re = re.compile('.*\ \[(.*)\ [\+-]\d\d\d\d]\ \".*')
increment = 1
while (increment <= count):
    log = None
    try:
        log = open(filename)
        for line in log.readlines():
            if (len(line) < 10):
                continue

            m = date_re.match(line)
            if (not m):
                sys.stderr.write("error: '%s'" % line)
                continue

            groups = m.groups()
            if (not groups):
                sys.stderr.write("error: '%s'" % line)
                continue

            date = datetime.strptime(groups[0], '%d/%b/%Y:%H:%M:%S')
            
            new_date = date + relativedelta(days=+increment)
            out.write(line.replace(groups[0], new_date.strftime("%d/%b/%Y:%H:%M:%S")))
    finally:
        if (not log):
            log.close()
    increment = increment + 1
    sys.stderr.write("%s\n" % increment)

import datetime

import plazma.lib.task.task_helper as this
import plazma.lib.sys.syslib as syslib
import plazma.lib.fmt.fmtlib as fmtlib

# print
TASK_PRINT_SYSTEM_INFO = "print-system-info"
TASK_PRINT_DATE = "print-date"
TASK_PRINT_TIME = "print-time"
TASK_PRINT_DATE_TIME = "print-date-time"

PARAMETER_FORMAT = "format"

# execute

def executePrintSystemInfo(parameters):
    print("System Info")

    print(" os.name       : " + syslib.getOsName())
    print(" os.version    : " + syslib.getOsVersion())
    print(" os.arch       : " + syslib.getOsArch())
    print(" os.arch.data  : " + syslib.getOsArchData())

    print(" user.name     : " + syslib.getUserName())
    print(" user.home     : " + syslib.getUserHome())
    print(" user.dir      : " + syslib.getUserDir())
    print(" tmp.dir       : " + syslib.getTmpDir())

    #print(" file.encoding : " + syslib.getEncoding())
    

def executePrintDate(parameters):
    format = getFormat(parameters)
    print(fmtlib.formatDate(today(), format))

def executePrintTime(parameters):
    format = getFormat(parameters)
    print(fmtlib.formatTime(now(), format))

def executePrintDateTime(parameters):
    format = getFormat(parameters)
    print(fmtlib.formatDateTime(now(), format))

def today():
    return datetime.date.today()

def now():
    return datetime.datetime.now()

##

def getFormat(parameters):
    format = this.getParameter(parameters, PARAMETER_FORMAT)
    return format

    '''
    size = len(format)
    start = 0
    end = size - 1

    # Unquote
    if (size > 2):
        if ((format[start] == "'" and format[end] == "'") or (format[start] == '"' and format[end] == '"')):
            format = format[start:size]

    return format
    '''


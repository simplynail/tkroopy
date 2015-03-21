# -*- coding: utf-8 -*-#

import src.tkroopy as tkroopy
import os, sys, datetime
import logging

format = '%(asctime)s::%(name)s - %(levelname)s - %(filename)s - %(lineno)d - %(message)s'
datefmt = '%Y%m%d %H:%M:%S'

if '__file__' in globals():
    basedir = os.path.dirname(os.path.abspath(__file__))
    logging.basicConfig(format=format, level=logging.NOTSET, datefmt=datefmt)
elif hasattr(sys, 'frozen'):
    basedir = os.path.dirname(os.path.abspath(sys.executable))  # for py2exe
    logging.basicConfig(format=format, level=logging.NOTSET, filename=r'logs\%s.log' % datetime.datetime.now().strftime("%Y%m%d"), datefmt=datefmt)
else:  # should never happen
    basedir = os.getcwd()
os.chdir(basedir)

sys.path = [basedir] + [p for p in sys.path if not p == basedir]

log = logging.getLogger(__package__)

log.info("--------------------------------------------------------------------")
log.info("Application Launched")
log.info("--------------------------------------------------------------------")


if __name__ == "__main__":
    try:
        from multiprocessing import freeze_support
        freeze_support()
    except:
        log.error('Freeze Support Error')

    try:
        app = tkroopy.tKroopy(basedir)
        app.mainloop()
    except Exception as e:
        log.error(e, exc_info=True)
    sys.exit()

# ------ END OF FILE ----
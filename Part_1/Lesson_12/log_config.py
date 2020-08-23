import logging
import traceback


logging.basicConfig(
    filename='app.log',
    filemode='a',
    format='%(name)s - %(levelname)s - %(asctime)s - %(message)s',
    level=logging.INFO
)

log_app =logging.getLogger('LOGG')

def log(func): 
    def decor(*args):
        main_func = traceback.extract_stack(None, 2)[0][2]
        name_func = func.__name__
        log_app.info('%s call is %s', name_func, main_func)
        result = func(*args)
        return result
    return decor



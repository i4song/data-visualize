import logging
import sys
import os
from logging.handlers import RotatingFileHandler
import datetime


def file_logger(level):
    serv_path = '/logs/'
    abs_path = os.getcwd()
    directory = abs_path + serv_path
    if not os.path.exists(directory):
        os.makedirs(directory)

    now = datetime.datetime.now()
    nowDate = now.strftime('%Y-%m-%d')
    nowDate += '_error.log'
    formatter = logging.Formatter(
        '%(asctime)s - LevelName : %(levelname)s in %(module)s [%(lineno)d]  Message : %(message)s')
    handler = RotatingFileHandler(directory + nowDate, maxBytes=10485760, backupCount=1)  # 10메가 기준임
    handler.setLevel(getattr(logging, level))
    handler.setFormatter(formatter)
    return handler

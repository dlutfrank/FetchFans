# encoding = utf8

log_level_debug = 0
log_level_info = 1
log_level_warn = 2
log_level_err = 3

log_level = log_level_debug


def log(level, tag, message):
    if level >= log_level:
        print(tag + ': ', end='')
        print(message)


def log_d(tag, message):
    log(log_level_debug, tag, message)


def log_i(tag, message):
    log(log_level_info, tag, message)


def log_w(tag, message):
    log(log_level_warn, tag, message)


def log_e(tag, message):
    log(log_level_err, tag, message)

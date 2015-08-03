class Debug(object):
    _log = []
    _warnings = []
    _verbose = False

    @staticmethod
    def log(source, msg):
        Debug._log.append((source, msg))
        if Debug._verbose:
            print("LOG: {}".format(msg))

    @staticmethod
    def warn(source, msg):
        Debug._warnings.append((source, msg))
        if Debug._verbose:
            print("WARNING: {}".format(msg))

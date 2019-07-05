import os


class Configuration(object):

    if 'RANCHER_URL' in os.environ:
        RANCHER_URL = os.environ['RANCHER_URL']
    else:
        RANCHER_URL = 'http://rancher-ui.local'

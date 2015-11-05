__author__ = 'bunjiboys'

import logging
from plugin_example_base import PluginManager

log = logging.getLogger()
logging.basicConfig(level='INFO', format='Module: %(name)-40s Message: %(message)s')

plugins = PluginManager()
plugins.run()

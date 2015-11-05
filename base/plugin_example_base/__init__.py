__author__ = 'bunjiboys'

import logging
from pkg_resources import iter_entry_points

log = logging.getLogger(__name__)

class PluginManager(object):
    __plugins = [ ]
    def __init__(self):
        for entry_point in iter_entry_points('plugin_example_base.plugins'):
            cls = entry_point.load()
            log.info('Discovered a new plugin: {plugin} @ {mod}'.format(plugin=entry_point.name, mod=entry_point.module_name))
            self.__plugins.append(cls)

    def run(self):
        for plugin_class in self.__plugins:
            # Create an object instances and execute an instance method
            plugin_instance = plugin_class()
            plugin_instance.run('Mr', 'Flibble\'s', mood='very cross')

            # Executing a static class method
            plugin_class.run_static('Mr', 'Flibble\'s', mood='is very cross')

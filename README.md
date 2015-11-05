# plugin_example
It would be advisable to run the following commands inside a python virtualenv to avoid "tainting" the default python environment with these modules.
```bash
# Clone repo and enter folder
git clone https://github.com/bunjiboys/plugin_example.git
cd plugin_example
# Install required python modules
pip install -r requirements.txt

# Install base module
(cd base && python setup.py install)

# Install 3rd-party module
(cd third_party && python setup.py install)

# Execute the example run script
python run.py
```

The above commands should result in something like
```
$ python run.py
Module: plugin_example_base                      Message: Discovered a new plugin: builtin @ plugin_example_base.plugins.builtin
Module: plugin_example_base                      Message: Discovered a new plugin: third_party @ third_party_plugin.plugins.third_party
Module: plugin_example_base.plugins.builtin      Message: run method executed. self: <plugin_example_base.plugins.builtin.BuiltInPlugin object at 0x10bd8ab50>, args: Mr, Flibble's, kwargs: mood=very cross
Module: plugin_example_base.plugins.builtin      Message: run_static method executed. args: Mr, Flibble's, kwargs: mood=is very cross
Module: third_party_plugin.plugins.third_party   Message: run method executed. self: <third_party_plugin.plugins.third_party.ThirdPartyPlugin object at 0x10be09850>, args: Mr, Flibble's, kwargs: mood=very cross
Module: third_party_plugin.plugins.third_party   Message: run_static method executed. args: Mr, Flibble's, kwargs: mood=is very cross
```

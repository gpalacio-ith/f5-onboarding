#!/usr/bin/python
from jinja2 import Template
import yaml

# Loads JSON/Jinja template
json_template = Template(open('templates/device-onboarding.jinja').read())

# Load data from YAML file into Python dictionary with variables
# that make the F5 DO final JSON to upload
file_path = './device-config.yaml'
with open(file_path) as config_file:
    device_config = yaml.load(config_file, Loader=yaml.FullLoader)

# Render template using data
json_string = json_template.render(device_config)
print(json_string)




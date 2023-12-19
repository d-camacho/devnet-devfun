from jinja2 import Template
import yaml

# Your YAML data
yaml_data = """
EEMs:
  name: MAIN
    - commands 
      - event manager applet {{ eem.name }} authorization bypass
      - event none maxrun 60
    - action    
      - "enable"
      - "configure terminal"
      - "interface f0/1"
      - sub_action
        - "description MAIN"
        - "switchport mode access vlan 100"
      - "end"

  name: BRANCH
    - commands
      - event manager applet {{ eem.name }} authorization bypass
      - event none maxrun 60
    - action    
      - "enable"
      - "configure terminal"
      - "interface f0/2"
      - sub_action
        - "description BRANCH"
        - "switchport mode access vlan 200"
      - "end"
"""

# Your Jinja template
jinja_template = """
{# Iterate through EEMs #}
{% for eem in EEMs %}
{% if eem.name in reqdEEMs %}
{% for command in eem.commands %}
{{ command }}
{% endfor %}
{% for action in eem.action %}
  action {{ loop.index }}.0 cli command "{{ action }}"
(% for action in action.sub_action)
  action {{ loop.parent.loop.index }}.{{ loop.index }} "{{ action }}"
{% endfor %}
{% endif %}
{% endfor %}


"""

# Create a Jinja template object
template = Template(jinja_template)

# Load YAML data into a dictionary
yaml_dict = yaml.safe_load(yaml_data)

# Render the template with the YAML data
output_text = template.render(reqdEEMs=["BRANCH"], EEMs=yaml_dict.get("EEMs", {}))

# Print the output
print(output_text)

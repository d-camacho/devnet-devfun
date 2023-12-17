from flask import Flask, render_template
import yaml

app = Flask(__name__)

@app.route('/')
def index():
    # Load YAML data from a separate file
    with open('data.yaml', 'r') as yaml_file:
        data = yaml.safe_load(yaml_file)

    # Render the template and pass the YAML data to the context
    return render_template('user_template.jinja2', user_data=data['user'])

if __name__ == '__main__':
    app.run(debug=True)

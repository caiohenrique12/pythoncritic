from jinja2 import Environment, FileSystemLoader

Environment(loader=FileSystemLoader('src/pythoncritic/templates'))
# template = env.get_template('dashboard.html')

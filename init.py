#!/usr/bin/env python3

import os
import sys
import subprocess
from pathlib import Path

# Define the project structure
project_structure = [
    '{project_name}/app',
    '{project_name}/app/templates',
    '{project_name}/app/static',
    '{project_name}/app/static/css',
    '{project_name}/app/static/js',
    '{project_name}/app/static/images',
]

# Boilerplate content for each file
files_content = {
    '__init__.py': '''from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    with app.app_context():
        # Import parts of our application
        from . import routes

        return app
''',

    'routes.py': '''from flask import current_app as app
from flask import render_template

@app.route('/')
def home():
    return render_template('base.html', title='Home')
''',

    'models.py': '''# Define your database models here
''',

    'config.py': '''import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
    DEBUG = True
''',

    'run.py': '''from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run()
''',

    'requirements.txt': '''Flask==2.3.2
''',

    'base.html': '''<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{{ title }} - Flask App</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
</head>
<body>
    <header>
        <h1>Welcome to {{ title }}</h1>
    </header>
    <main>
        <p>Your content goes here.</p>
    </main>
    <script src="{{ url_for('static', filename='js/scripts.js') }}"></script>
</body>
</html>
''',

    'styles.css': '''/* Add your custom styles here */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0.
}
''',

    'scripts.js': '''// Add your custom JavaScript here
console.log('JavaScript is working!');
''',

    '.gitignore': '''venv/
__pycache__/
*.pyc
instance/
.env
'''
}

def create_project(project_name):
    # Create directories
    for path in project_structure:
        dir_path = Path(path.format(project_name=project_name))
        dir_path.mkdir(parents=True, exist_ok=True)
        print(f'Created directory: {dir_path}')

    # Create files with boilerplate content
    files_to_create = {
        f'{project_name}/app/__init__.py': files_content['__init__.py'],
        f'{project_name}/app/routes.py': files_content['routes.py'],
        f'{project_name}/app/models.py': files_content['models.py'],
        f'{project_name}/config.py': files_content['config.py'],
        f'{project_name}/run.py': files_content['run.py'],
        f'{project_name}/requirements.txt': files_content['requirements.txt'],
        f'{project_name}/app/templates/base.html': files_content['base.html'],
        f'{project_name}/app/static/css/styles.css': files_content['styles.css'],
        f'{project_name}/app/static/js/scripts.js': files_content['scripts.js'],
        f'{project_name}/.gitignore': files_content['.gitignore'],
    }

    for file_path, content in files_to_create.items():
        with open(file_path, 'w') as file:
            file.write(content)
            print(f'Created file: {file_path}')

    # Set up virtual environment and install dependencies
    venv_path = Path(f'{project_name}/venv')
    print('Creating virtual environment...')
    subprocess.run([sys.executable, '-m', 'venv', str(venv_path)])

    # Determine the correct path for the pip executable
    pip_executable = venv_path / 'bin' / 'pip'
    if os.name == 'nt':  # Windows
        pip_executable = venv_path / 'Scripts' / 'pip.exe'

    # Install Flask and dependencies
    print('Installing Flask and dependencies...')
    subprocess.run([str(pip_executable), 'install', '-r', f'{project_name}/requirements.txt'])

    print(f'\nProject "{project_name}" has been created successfully!')
    print(f'To get started:')
    if os.name == 'nt':
        print(f'1. Navigate to the project directory:\n   cd {project_name}')
        print(f'2. Activate the virtual environment:\n   {venv_path}\\Scripts\\activate')
    else:
        print(f'1. Navigate to the project directory:\n   cd {project_name}')
        print(f'2. Activate the virtual environment:\n   source {venv_path}/bin/activate')
    print(f'3. Run the application:\n   python run.py')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python initialize_project.py project_name')
    else:
        project_name = sys.argv[1]
        create_project(project_name)


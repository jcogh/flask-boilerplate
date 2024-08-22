# Flask Starter Template

This repository serves as a template for starting new Flask projects. It provides a basic project structure and a Python script to initialize a new Flask project with bare-bones functionality.

## Project Structure

After running the initialization script, your new Flask project will have the following structure:

```plaintext
your_project_name/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   ├── templates/
│   │   └── base.html
│   └── static/
│       ├── css/
│       │   └── styles.css
│       ├── js/
│       │   └── scripts.js
│       └── images/
│
├── venv/
│
├── config.py
│
├── requirements.txt
│
├── run.py
│
└── .gitignore
```

## Usage
```
git clone https://github.com/yourusername/flask-boilerplate.git
cd flask-boilerplate

python initialize_project.py your_project_name

cd your_project_name

source venv/bin/activate  # On Windows: venv\Scripts\activate

python run.py
```

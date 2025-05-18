
```markdown
# Portfolio Website

Welcome to my portfolio website project! This site showcases my work, skills, and projects with a clean, comic-style design.

## About

This project is a personal portfolio website built using Flask, featuring a JSON-based project database and local image assets. The site uses Jinja2 templating for dynamic rendering and is styled with custom CSS for a unique comic panel aesthetic.

## Features

- Dynamic loading of project data from a JSON file  
- Responsive design with comic-style panels and speech bubbles  
- Local image assets for fast loading and offline availability  
- Easy to maintain and extend with new projects and skills  

## Project Structure

```

project/
│
├── static/
│   ├── css/
│   ├── js/
│   ├── assets/img/
│   └── data/
│       └── projects.json
│
├── templates/
│   └── index.html
│
├── app.py
├── requirements.txt
├── .gitignore
├── Procfile
└── README.md

````

## Getting Started

### Prerequisites

- Python 3.x  
- pip  

### Installation

1. Clone the repository:

```bash
git clone https://github.com/ArjunPathania/data_hero.git
cd data_hero
````

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the Flask app:

```bash
python app.py
```

4. Open your browser at `http://localhost:5000`

## Deployment

This project can be deployed on free hosting platforms like Render or Heroku, as it only requires a lightweight Flask app and serves static files locally. Make sure to include a `Procfile` and push the local images and JSON data along with your code.

## Contact

**Arjun Pathania**
Email: [arjunpathania786f@gmail.com](mailto:arjunpathania786f@gmail.com)
GitHub: [https://github.com/ArjunPathania/data\_hero](https://github.com/ArjunPathania/data_hero)
Portfolio:[DataHero](https://data-hero.onrender.com)

```

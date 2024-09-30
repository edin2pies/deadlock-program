# Django Game Item Recommender

This Django web application is designed to provide item recommendations for the game *Deadlock*. It helps players choose the best items to counter opposing heroes in this MOBA-style game with shooter elements.

## Features
- Item recommendations based on enemy team composition.
- User-friendly interface for hero selection and viewing item suggestions.
- Easy setup and deployment with static files managed.

## Prerequisites

Ensure you have the following installed on your machine:
- Python 3.x
- Django 3.x+
- Git
- Virtualenv (optional but recommended)

## Setup and Installation

Follow these steps to set up the project locally:

### 1. Clone the Repository

```bash
git clone https://github.com/edin2pies/deadlock-program.git
cd game-item-recommender
```

### 2. Create a Virtual Environment (optional)

```bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Collect Static Files with

```bash
python manage.py collectstatic
```

### 5. Apply Migrations

```bash
python manage.py migrate
```

### 6. Run the Server

```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000/ in your browser to see the app in action.

## Contributing

Feel free to fork the project, make improvements, and submit pull requests.

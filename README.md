**GameVault** is a personal video game database web application built with Django. Browse, search, filter, and sort your favourite games — complete with cover art, studio info, platform details, Metacritic scores, and more.

> Created as part of a Master's degree in Applied Informatics at IHU University.

---

## Features

- **Home page** with a clean, minimal landing experience
- **Game catalogue** with a responsive card grid
- **Search** games by title (live client-side filtering)
- **Filter** by category and platform
- **Sort** by title, Metacritic score, or release date (ascending/descending)
- **Hover previews** on game cards showing cover art and a short description
- **Game detail pages** with full info: studio, platforms, release date, description, Metacritic score & link
- **Django Admin** panel for managing all data (games, studios, platforms, categories)
- **Dark/light theme** support via CSS variables
- Deployed on **PythonAnywhere**

---

## Tech Stack

| Layer     | Technology           |
|-----------|----------------------|
| Backend   | Python 3 / Django 5  |
| Database  | SQLite               |
| Frontend  | HTML, CSS, Vanilla JS |
| Media     | Django media file handling |
| Hosting   | PythonAnywhere       |


## Data Models

- **Game** — title, description, cover image, release date, Metacritic score & URL, user rating, linked studio, categories, and platforms
- **Studio** — name, founding date, country, bio, logo
- **Platform** — name, manufacturer, release date
- **Categories** — name

---

## Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/GameVault.git
cd GameVault

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install django pillow python-dotenv

# Apply database migrations
python manage.py migrate

# Create a superuser for the admin panel
python manage.py createsuperuser

# Run the development server
python manage.py runserver
```

## Usage

- Visit `/` for the home page
- Visit `/games/` to browse and search the full game catalogue
- Visit `/games/<id>/` for a game's detail page
- Visit `/admin/` to manage all content via the Django admin panel

---

## License

This project was created for academic purposes. Feel free to use it as a reference or starting point for your own projects.

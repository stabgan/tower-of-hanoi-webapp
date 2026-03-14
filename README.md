# 🗼 Tower of Hanoi — Interactive Web Visualization

An interactive, browser-based visualization of the classic **Tower of Hanoi** puzzle. Enter any number of discs and watch the recursive algorithm solve it step-by-step with smooth canvas animations and adjustable speed control.

---

## ✨ Features

- 🎮 Choose the number of discs and visualize the full solution
- ⚡ Adjustable animation speed via a range slider
- 📊 Live step counter displayed on the canvas
- 🧮 Classic recursive algorithm implemented in Python
- 🌐 Lightweight single-page web app served with Flask

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| 🐍 Backend | **Python 3** · **Flask** |
| 📝 Forms | **Flask-WTF** · **WTForms** |
| 🎨 Frontend | **Vanilla JavaScript** · **HTML5 Canvas** |
| 🚀 Deployment | **Gunicorn** · Heroku-ready (`Procfile` included) |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.6+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/stabgan/tower-of-hanoi-webapp.git
cd tower-of-hanoi-webapp

# Install dependencies
pip install -r requirements.txt

# Run the app
python hanoi.py
```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

### Deploy to Heroku

The project includes a `Procfile` for one-click Heroku deployment:

```bash
heroku create
git push heroku master
```

---

## ⚠️ Known Issues

- **High disc counts can hang the server** — the recursive solver runs synchronously on the backend, so very large inputs (e.g. > 20 discs) may cause long response times or timeouts.
- **Canvas sizing** — the visualization is laid out with fixed pixel offsets; on very narrow viewports the discs may overlap or clip.
- **No input validation cap** — there is no upper-bound check on the disc count input, which can lead to the recursion depth issue above.
- **`eval()` usage in the frontend** — Jinja template variables are injected into JavaScript via `eval()`, which is functional but not ideal from a security standpoint.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE) — © 2019 Kaustabh Ganguly.

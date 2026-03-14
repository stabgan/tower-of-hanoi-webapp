# Tower of Hanoi — Interactive Web Visualizer

A browser-based Tower of Hanoi solver and step-by-step animator built with Flask and vanilla JavaScript.

## What It Does

Enter the number of discs and watch the classic recursive algorithm play out on an HTML5 canvas. A slider lets you control animation speed in real time.

## How It Works

1. The Flask backend solves the puzzle recursively, recording every move as a `[source, destination]` pair.
2. The move sequence is injected into the template as JSON.
3. Client-side JavaScript replays the moves on a `<canvas>`, drawing and clearing disc stacks frame by frame.

## 🛠 Tech Stack

| Layer | Technology |
|-------|-----------|
| 🐍 Backend | Flask, Flask-WTF, WTForms |
| 🎨 Frontend | Vanilla JS, HTML5 Canvas |
| 🚀 Deployment | Gunicorn, Heroku-ready (`Procfile`) |

## Getting Started

```bash
# Clone
git clone https://github.com/stabgan/tower-of-hanoi-webapp.git
cd tower-of-hanoi-webapp

# Install dependencies
pip install -r requirements.txt

# Run locally
python hanoi.py
# → Open http://127.0.0.1:5000
```

## Deploy to Heroku

The included `Procfile` is ready to go:

```bash
heroku create
git push heroku master
```

## ⚠️ Known Issues

- Large disc counts (>15) will hit Python's default recursion limit and may hang the server. Input is capped at 15 via form validation.
- The canvas layout uses fixed pixel offsets — it works well on desktop but isn't fully responsive on narrow mobile screens.

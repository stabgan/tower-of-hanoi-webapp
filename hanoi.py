"""Tower of Hanoi — Flask web application with animated visualization."""

import os

from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import NumberRange, InputRequired


class Tower:
    """Solve the Tower of Hanoi puzzle and record every move."""

    def __init__(self):
        self.count = 0
        self.seq = []

    def hanoi(self, n, src, aux, dst):
        """Recursively solve for *n* discs, recording each move."""
        if n > 0:
            self.hanoi(n - 1, src, dst, aux)
            self.seq.append([src, dst])
            self.count += 1
            self.hanoi(n - 1, aux, src, dst)
        return self.count


# ---------------------------------------------------------------------------
# Flask application
# ---------------------------------------------------------------------------

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "change-me-in-production")


class DiscForm(FlaskForm):
    """Simple form that accepts the number of discs."""

    num = IntegerField(
        "Enter the number of discs: ",
        validators=[InputRequired(), NumberRange(min=1, max=15)],
    )
    submit = SubmitField("Submit")


@app.route("/", methods=["GET", "POST"])
def index():
    """Render the main page and compute the solution when the form is submitted."""
    num = 4  # sensible default
    form = DiscForm()

    if form.validate_on_submit():
        num = form.num.data
        form.num.data = ""

    solver = Tower()
    steps = solver.hanoi(num, 1, 2, 3)

    return render_template(
        "index.html",
        count=steps,
        seq=solver.seq,
        discs=num,
        form=form,
    )


if __name__ == "__main__":
    app.run(debug=True)

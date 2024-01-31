from flask import Flask, jsonify, render_template, request, redirect
import uuid

from models import storage
from models.measure import Measure

app = Flask(__name__)
@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()

@app.route('/', strict_slashes=False)
def home():
    """ HBNB is alive! """
    measures = storage.all("Measure").values()
    st_ct = []


    return render_template('home.html',
                           measures=measures,
                           cache_id=uuid.uuid4())

@app.route("/new", strict_slashes=False, methods=['GET', 'POST'])
def nouvelle_mesure():
    if request.method == 'POST':
        keys = []
        data = request.form.to_dict()
        for k, v in data.items():
            if v == '':
                keys.append(k)
        for k in keys:
            del data[k]
        measure = Measure(**data)
        measure.save()
        return redirect('/')
    return render_template('new_measure.html')

@app.route("/views", strict_slashes=False)
def views():
    measures = storage.all('Measure').values()
    return render_template('view.html', measures=measures)

@app.route("/view_edit", strict_slashes=False)
def view_edit():
    measures = storage.all('Measure').values()
    return render_template('view_edit.html', measures=measures)

if __name__ == "__main__":
    app.run(debug=True)
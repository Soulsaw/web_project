#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Places """
from models.measure import Measure
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request


@app_views.route('/measures', methods=['GET', 'POST'],
                 strict_slashes=False)
def get_measures():
    """
    Retrieves the list of all Place objects of a City
    """
    if request.method == 'POST':
            if not request.get_json():
                abort(400, description="Not a JSON")
            if 'first_name' not in request.get_json():
                abort(400, description="Missing first_name")
            if 'last_name' not in request.get_json():
                    abort(400, description="Missing last_name")
            data = request.get_json()
            measure = Measure(**data)
            measure.save()
            return make_response(jsonify(measure.to_dict()), 201)
    
    measures = storage.all(Measure).values()
    measures = [measure.to_dict() for measure in measures]
    return jsonify(measures)

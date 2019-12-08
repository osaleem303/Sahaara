from flask import Flask, jsonify, request
from data import Event
from DB import DB


app = Flask(__name__)


@app.route('/notify/<str:id>/<str:long>/<str:lat>')
def notify(id, long, lat):
    from logic import Location
    l = Location
    l.get_guardians()
    l.get_locations()
    l.find_candidates()
    l.notify()

@app.route('/update-zones')
def update():
    l = Event()
    l.get_data()
    l.calc_hotzones()
    l.update_zone()

@app.route('/get_zones')
def get_zones():
    table = DB.get_table('zones')
    zones = [x.to_dict() for x in table.steam()]
    return jsonify({'zones': zones})







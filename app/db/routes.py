from app.db.functions import exec_query, read_files
from app.db.queries import GET_CONTRIES, get_city_by_state, get_state_by_contry

from . import data


@data.route("/countries")
def get_contries():
    contries, states, cities = read_files()
    df = exec_query(contries, states, cities, GET_CONTRIES)
    result = []
    for row in df.values:
        result.append({
            "id_country": row[0],
            "name": row[1]
        })
    return {"countries": result}


@data.route("/states/<country_id>")
def get_states(country_id):
    contries, states, cities = read_files()
    df = exec_query(contries, states, cities, get_state_by_contry(country_id))
    result = []
    for row in df.values:
        result.append({
            "id_state": row[0],
            "name": row[1],
            "id_country": row[2],
        })
    return {"state": result}


@data.route("/cities/<state_id>")
def get_cities(state_id):
    contries, states, cities = read_files()
    df = exec_query(contries, states, cities, get_city_by_state(state_id))
    result = []
    for row in df.values:
        result.append({
            "id_city": row[0],
            "name": row[1],
            "id_state": row[2],
            "population": row[3]
        })
    return {"city": result}

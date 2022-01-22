GET_CONTRIES = "SELECT * FROM countries;"
GET_STATES = "SELECT * FROM states;"
GET_CITIES = "SELECT * FROM cities;"


def get_state_by_contry(contry_id):
    return f"SELECT * FROM states WHERE ID_COUNTRY={contry_id}"


def get_city_by_state(state_id):
    return f"SELECT * FROM cities WHERE ID_STATE={state_id}"

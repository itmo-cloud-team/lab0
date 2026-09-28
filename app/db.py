import mariadb
from datetime import datetime

db_connection = None
db_cursor = None

def connect(username, password, host, port, name):
    try:
        global db_connection, db_cursor

        db_connection = mariadb.connect(
            user=username,
            password=password,
            host=host,
            port=port,
            database=name
        )
        db_cursor = db_connection.cursor()
        print('[i] Connected to DB successfully.')
        return True
    except mariadb.Error as e:
        print(f'Error while connecting to DB. Error text: {e}')
        return False

def list_aircraft():
    global db_cursor
    db_cursor.execute('SELECT * FROM aircraft')
    result = db_cursor.fetchall()
    aircraft = []
    for tail_number, production_date, aircraft_type in result:
        readable_date = production_date.strftime('%Y-%m-%d')
        aircraft.append({
            'tailNumber': tail_number,
            'productionDate': readable_date,
            'icaoAircraftType': aircraft_type
        })
    return aircraft

def enlist_aircraft(tail_number, production_date, aircraft_type):
    try:
        global db_cursor, db_connection
        db_cursor.execute(
            (f'INSERT INTO aircraft( '
                'tail_number, '
                'production_date, '
                'icao_aircraft_type'
              ') VALUES (?, FROM_UNIXTIME(?), ?)'),
            (tail_number, production_date, aircraft_type)
        )
        db_connection.commit()
        return True
    except Exception as e:
        print(e)
        return False

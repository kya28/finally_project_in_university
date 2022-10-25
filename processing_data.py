import psycopg2


def select_data():
    con = psycopg2.connect(
        database="ammonia",
        user="postgres",
        password="1",
        host="127.0.0.1",
        port="5432"
    )
    cur = con.cursor()
    cur.execute(
        "SELECT con_data.date, con_data.concentration, factors.temperature, factors.speed, factors.humidity, factors.pressure from con_data inner join factors on con_data.date = factors.date ")
    rows = cur.fetchall()
    con.close()
    return rows


def func_drop_bd(date):
    con = psycopg2.connect(
        database="ammonia",
        user="postgres",
        password="1",
        host="127.0.0.1",
        port="5432"
    )
    cur = con.cursor()
    cur.execute(f"DELETE from con_data where date='{date}';")
    con.commit()
    cur.execute(
        "SELECT con_data.date, con_data.concentration, "
        "factors.temperature, factors.speed, factors.humidity, "
        "factors.pressure from con_data inner join factors "
        "on con_data.date = factors.date ")


def add_data(date, concentration, temperature, speed, humidity, pressure):
    con = psycopg2.connect(
        database="ammonia",
        user="postgres",
        password="1",
        host="127.0.0.1",
        port="5432"
    )
    cur = con.cursor()
    cur.execute(
        f"INSERT INTO con_data (date, concentration)  VALUES ('{date}', '{concentration}')")
    cur.execute(
        f"INSERT INTO factors (date, temperature, speed, humidity, pressure) VALUES ('{date}', '{temperature}', '{speed}', '{humidity}', '{pressure}')")
    con.commit()
    con.close()

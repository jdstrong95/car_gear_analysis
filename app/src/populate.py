import sqlite3
import sqlite3 as sl
import logging
logging.basicConfig(level=logging.INFO)

from app.src.models.errors import ErrorCodes

from app.src.models.car import Car


class CreateTablesException(Exception):
    pass


def create_tables() -> None:
    """
    Creates the required tables in the database
    :return: None
    """
    con = sl.connect('../db/cars.db')

    with open('../db/create_tables.sql', 'r') as f:
        sql = f.read()

        sql_commands = sql.split(';')

        # Execute each SQL command within the file
        for command in sql_commands:
            try:
                logging.info(command)
                with con:
                    con.execute(command)
            except Exception as e:
                logging.error(e)
                raise CreateTablesException(e)


def populate_table(sql: str, data: list[tuple]) -> None:
    """
    Populates table using the executemany method
    :param sql: SQL
    :param data: list of tuples representing the values()
    :return:
    """

    con = sl.connect('../db/cars.db')
    with con:
        try:
            logging.info(f'Executing: {sql}')
            logging.info(f'Data: {data}')
            con.executemany(sql, data)
        except sqlite3.IntegrityError as e:
            logging.error(e)
            logging.error("Table already populated!")


def populate_car_models() -> None:
    """
    Populates the car_models table
    :return:
    """

    sample_data = [
        ('Corolla', 2023),
        ('Corolla', 2022),
        ('Corolla', 2021),
        ('Corolla', 2020),
        ('Yaris', 2023),
        ('Yaris', 2022),
        ('Yaris', 2021),
        ('Yaris', 2020),
        ('Camry', 2023),
        ('Camry', 2022),
        ('Camry', 2021),
        ('Camry', 2020),
        ('Sienna', 2023),
        ('Sienna', 2022),
        ('Sienna', 2021),
        ('Sienna', 2020),
    ]

    sql = 'INSERT INTO car_models (name, year) values (?,?)'

    populate_table(sql, sample_data)


def populate_error_codes() -> None:
    """
    Populates the error_codes table
    :return:
    """

    sample_data = [
        (ErrorCodes(1).value, ErrorCodes(1).name),
        (ErrorCodes(2).value, ErrorCodes(2).name),
        (ErrorCodes(3).value, ErrorCodes(3).name)
    ]

    sql = 'INSERT INTO error_codes (id, name) values (?, ?)'

    populate_table(sql, sample_data)


def main():
    # Create tables
    create_tables()

    # Populate the car_models table
    populate_car_models()

    # Populate the error_codes table
    populate_error_codes()

if __name__ == '__main__':
    main()

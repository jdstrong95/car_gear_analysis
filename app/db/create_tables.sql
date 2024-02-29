
CREATE TABLE IF NOT EXISTS error_codes
(
    id   integer not null primary key autoincrement,
    name text,
    unique (name)
);


CREATE TABLE IF NOT EXISTS car_models
(
    id  integer not null primary key AUTOINCREMENT,
    name text not null,
    year integer
);

CREATE TABLE IF NOT EXISTS cars
(
    id         integer not null primary key AUTOINCREMENT,
    vin_number integer not null,
    FOREIGN KEY (vin_number) REFERENCES car_models(id)
);

CREATE TABLE IF NOT EXISTS car_malfunctions
(
    id         integer  not null primary key autoincrement,
    car_id     integer  not null,
    error_code smallint not null,
    created_at timestamp,
    foreign key (car_id) references cars (id),
    foreign key (error_code) references error_codes (id)
);

CREATE TABLE IF NOT EXISTS gear_shifts
(
    id         integer  not null primary key autoincrement,
    car_id     integer  not null,
    speed      integer  not null,
    gear       smallint not null,
    created_at timestamp,
    foreign key (car_id) references cars (id)
);

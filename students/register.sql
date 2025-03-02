

-- create students table
CREATE TABLE students(
    id INTEGER,
    firstname TEXT NOT NULL,
    middlename TEXT,
    lastname TEXT NOT NULL,
    gender TEXT NOT NULL,
    date_of_birth TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT NOT NULL,

    PRIMARY KEY(id)
);
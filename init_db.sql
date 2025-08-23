DROP TABLE IF EXISTS issues;
CREATE TABLE issues (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    category TEXT,
    lat REAL,
    lon REAL,
    image TEXT,
    reporter TEXT,
    status TEXT,
    created_at TEXT
);

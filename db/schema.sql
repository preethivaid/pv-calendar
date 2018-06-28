CREATE TABLE secrets (
    id SERIAL PRIMARY KEY,
    secret_key varchar(80),
    secret_value varchar(80)
);
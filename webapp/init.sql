CREATE DATABASE flask;

CREATE TABLE users (
	email		char(254) PRIMARY KEY NOT NULL,
	approved	boolean NOT NULL,
	admin		boolean NOT NULL
);

INSERT INTO users VALUES ('test@mibura.com', TRUE, TRUE);

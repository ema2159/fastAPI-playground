CREATE DATABASE IF NOT EXISTS fastapi_mysql_app;
USE fastapi_mysql_app;

CREATE TABLE IF NOT EXISTS `user` (
	id BIGINT NOT NULL,
	first_name VARCHAR(100),
	last_name VARCHAR(100),
	email VARCHAR(100),
	address VARCHAR(100),
	phone_num VARCHAR(100),
	PRIMARY KEY (id),
	UNIQUE (email)
);

CREATE TABLE IF NOT EXISTS bank_transaction (
       id INT NOT NULL,
       amount INT,
       timestamp DATETIME,
       sender_id BIGINT,
       receiver_id BIGINT,
       PRIMARY KEY (id),
       FOREIGN KEY(sender_id) REFERENCES `user` (id),
       FOREIGN KEY(receiver_id) REFERENCES `user` (id)
);

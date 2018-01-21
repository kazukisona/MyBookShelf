DROP TABLE IF EXISTS tb_book;

CREATE TABLE tb_book(
	id INT NOT NULL AUTO_INCREMENT,
	author VARCHAR(200) NOT NULL,
	publisher VARCHAR(100) NOT NULL,
	published_date DATE,
	isbn VARCHAR(20) NOT NULL,
	buying_date DATE,
	PRIMARY KEY(id)
);

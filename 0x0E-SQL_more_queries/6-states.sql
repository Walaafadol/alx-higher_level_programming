-- Write a script that creates the database hbtn_0d_usa and the table states
CREATE database IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(id INT NOT NULL, UNIQUE(ID),
AUTO_INCREMENT(ID), PRIMARY KEY(ID), name VARCHAR(256) NOT NULL);

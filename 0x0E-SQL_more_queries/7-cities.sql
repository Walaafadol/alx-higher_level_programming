-- Write a script that creates the database hbtn_0d_usa and the table states
CREATE database IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(
	id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
	state_id INT NOT NULL,
	FOREIGN KEy(state_id), REFERENCES hbtn_0d_usa.states(id),
	name VARCHAR(256) NOT NULL);

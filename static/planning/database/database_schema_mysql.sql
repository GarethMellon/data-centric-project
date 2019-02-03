CREATE TABLE `recipes` (
	`ID` INT NOT NULL AUTO_INCREMENT,
	`name` varchar(255) NOT NULL,
	`youtube_link` varchar(255) NOT NULL,
	`delete` BINARY NOT NULL DEFAULT 'false',
	PRIMARY KEY (`ID`)
);

CREATE TABLE `course` (
	`ID` INT NOT NULL AUTO_INCREMENT,
	`recipes_ID` INT NOT NULL,
	`name` varchar(255) NOT NULL,
	`delete` BINARY NOT NULL DEFAULT 'false',
	PRIMARY KEY (`ID`)
);

CREATE TABLE `cuisine` (
	`ID` INT NOT NULL AUTO_INCREMENT,
	`recipes_ID` INT NOT NULL,
	`name` varchar(255) NOT NULL,
	`delete` BINARY NOT NULL DEFAULT 'false',
	PRIMARY KEY (`ID`)
);

CREATE TABLE `allergens` (
	`ID` INT NOT NULL AUTO_INCREMENT,
	`recipes_ID` INT NOT NULL,
	`name` varchar(255) NOT NULL,
	`delete` BINARY NOT NULL DEFAULT 'delete',
	PRIMARY KEY (`ID`)
);

CREATE TABLE `ingredients` (
	`ID` INT NOT NULL AUTO_INCREMENT,
	`recipes_ID` INT NOT NULL,
	`name` varchar(255) NOT NULL,
	`quantity` varchar(10) NOT NULL,
	`unit_of_measurement` varchar(10) NOT NULL,
	`delete` BINARY NOT NULL DEFAULT 'false',
	PRIMARY KEY (`ID`)
);

CREATE TABLE `directions` (
	`ID` INT NOT NULL AUTO_INCREMENT,
	`recipes_ID` INT NOT NULL,
	`name` varchar(255) NOT NULL,
	`delete` BINARY NOT NULL DEFAULT 'false',
	PRIMARY KEY (`ID`)
);

CREATE TABLE `allergens_list` (
	`ID` INT(255) NOT NULL AUTO_INCREMENT,
	`allergens_id` INT NOT NULL,
	`name` varchar(255) NOT NULL,
	PRIMARY KEY (`ID`)
);

CREATE TABLE `course_list` (
	`ID` INT NOT NULL AUTO_INCREMENT,
	`course_id` INT NOT NULL,
	`name` varchar(255) NOT NULL,
	PRIMARY KEY (`ID`)
);

CREATE TABLE `cuisine_list` (
	`ID` BINARY NOT NULL AUTO_INCREMENT,
	`cuisine_ID` INT NOT NULL AUTO_INCREMENT,
	`name` INT NOT NULL,
	PRIMARY KEY (`ID`)
);

ALTER TABLE `course` ADD CONSTRAINT `course_fk0` FOREIGN KEY (`recipes_ID`) REFERENCES `recipes`(`ID`);

ALTER TABLE `cuisine` ADD CONSTRAINT `cuisine_fk0` FOREIGN KEY (`recipes_ID`) REFERENCES `recipes`(`ID`);

ALTER TABLE `allergens` ADD CONSTRAINT `allergens_fk0` FOREIGN KEY (`recipes_ID`) REFERENCES `recipes`(`ID`);

ALTER TABLE `ingredients` ADD CONSTRAINT `ingredients_fk0` FOREIGN KEY (`recipes_ID`) REFERENCES `recipes`(`ID`);

ALTER TABLE `directions` ADD CONSTRAINT `directions_fk0` FOREIGN KEY (`recipes_ID`) REFERENCES `recipes`(`ID`);

ALTER TABLE `allergens_list` ADD CONSTRAINT `allergens_list_fk0` FOREIGN KEY (`allergens_id`) REFERENCES `allergens`(`ID`);

ALTER TABLE `course_list` ADD CONSTRAINT `course_list_fk0` FOREIGN KEY (`course_id`) REFERENCES `course`(`ID`);

ALTER TABLE `cuisine_list` ADD CONSTRAINT `cuisine_list_fk0` FOREIGN KEY (`cuisine_ID`) REFERENCES `cuisine`(`ID`);


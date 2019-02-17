CREATE TABLE `recipes` (
	`ID` INT NOT NULL AUTO_INCREMENT,
	`name` varchar(255) NOT NULL,
	`youtube_link` varchar(255),
	`delete` BINARY NOT NULL DEFAULT '0',
	PRIMARY KEY (`ID`)
);

CREATE TABLE `course` (
	`ID` INT NOT NULL AUTO_INCREMENT,
	`recipes_ID` INT NOT NULL,
	`name` varchar(255) NOT NULL,
	`delete` BINARY NOT NULL DEFAULT '0',
	PRIMARY KEY (`ID`)
);

CREATE TABLE `cuisine` (
	`ID` INT NOT NULL AUTO_INCREMENT,
	`recipes_ID` INT NOT NULL,
	`name` varchar(255) NOT NULL,
	`delete` BINARY NOT NULL DEFAULT '0',
	PRIMARY KEY (`ID`)
);

CREATE TABLE `allergens` (
	`ID` INT NOT NULL AUTO_INCREMENT,
	`recipes_ID` INT NOT NULL,
	`name` varchar(255) NOT NULL,
	`delete` BINARY NOT NULL DEFAULT '0',
	PRIMARY KEY (`ID`)
);

CREATE TABLE `ingredients` (
	`ID` INT NOT NULL AUTO_INCREMENT,
	`recipes_ID` INT NOT NULL,
	`name` varchar(255) NOT NULL,
	`quantity` varchar(10),
	`unit_of_measurement` varchar(50),
	`delete` BINARY NOT NULL DEFAULT '0',
	PRIMARY KEY (`ID`)
);

CREATE TABLE `directions` (
	`ID` INT NOT NULL AUTO_INCREMENT,
	`recipes_ID` INT NOT NULL,
	`name` varchar(512) NOT NULL,
	`delete` BINARY NOT NULL DEFAULT '0',
	PRIMARY KEY (`ID`)
);

CREATE TABLE `allergens_list` (
	`ID` INT(255) NOT NULL AUTO_INCREMENT,
	`allergens_id` INT,
	`name` varchar(255) NOT NULL,
	PRIMARY KEY (`ID`)
);

CREATE TABLE `course_list` (
	`ID` INT NOT NULL AUTO_INCREMENT,
	`course_id` INT,
	`name` varchar(255) NOT NULL,
	PRIMARY KEY (`ID`)
);

CREATE TABLE `cuisine_list` (
	`ID` INT NOT NULL AUTO_INCREMENT,
	`cuisine_ID` INT,
	`name` varchar(255) NOT NULL,
	PRIMARY KEY (`ID`)
);

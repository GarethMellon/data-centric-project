ALTER TABLE `course` DROP FOREIGN KEY `course_fk0`;

ALTER TABLE `cuisine` DROP FOREIGN KEY `cuisine_fk0`;

ALTER TABLE `allergens` DROP FOREIGN KEY `allergens_fk0`;

ALTER TABLE `ingredients` DROP FOREIGN KEY `ingredients_fk0`;

ALTER TABLE `directions` DROP FOREIGN KEY `directions_fk0`;

ALTER TABLE `allergens_list` DROP FOREIGN KEY `allergens_list_fk0`;

ALTER TABLE `course_list` DROP FOREIGN KEY `course_list_fk0`;

ALTER TABLE `cuisine_list` DROP FOREIGN KEY `cuisine_list_fk0`;

DROP TABLE IF EXISTS `recipes`;

DROP TABLE IF EXISTS `course`;

DROP TABLE IF EXISTS `cuisine`;

DROP TABLE IF EXISTS `allergens`;

DROP TABLE IF EXISTS `ingredients`;

DROP TABLE IF EXISTS `directions`;

DROP TABLE IF EXISTS `allergens_list`;

DROP TABLE IF EXISTS `course_list`;

DROP TABLE IF EXISTS `cuisine_list`;

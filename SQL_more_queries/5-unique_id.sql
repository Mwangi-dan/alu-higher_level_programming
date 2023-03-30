-- Creates table unique_id with default value and being unique
CREATE TABLE IF NOT EXISTS unique_id (
	`id` INT UNIQUE,
	`name` VARCHAR(256)
);

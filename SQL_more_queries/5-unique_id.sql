-- Creates table unique_id with default value and being unique
CREATE TABLE IF NOT EXISTS unique_id (
	`id` INT DEFAULT 1 UNIQUE,
	`name` VARCHAR(256)
);

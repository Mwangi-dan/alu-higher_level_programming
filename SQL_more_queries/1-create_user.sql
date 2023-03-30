-- Creates MYSQL server user_0d_1
-- `user_0d_1` has all privileges 
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL TO 'user_0d_1'@'localhost';

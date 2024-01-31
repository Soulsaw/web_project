-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS web_dev_db;
CREATE USER IF NOT EXISTS 'web_dev'@'localhost' IDENTIFIED BY 'web_dev_pwd';
GRANT ALL PRIVILEGES ON `web_dev_db`.* TO 'web_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'web_dev'@'localhost';
FLUSH PRIVILEGES;

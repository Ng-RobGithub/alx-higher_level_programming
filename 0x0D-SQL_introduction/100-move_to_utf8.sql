-- Create and use the hbtn_0c_0 database
-- Create the first_table table
CREATE DATABASE IF NOT EXISTS hbtn_0c_0;
USE hbtn_0c_0;

CREATE TABLE IF NOT EXISTS first_table (
    id INT(11) AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) COLLATE utf8mb4_unicode_ci
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

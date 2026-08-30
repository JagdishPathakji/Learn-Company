-- database name
CREATE DATABASE knowledge_base;

-- refering to this database for next set of sql statements
USE knowledge_base;

-- this table is for the different roles provided 
CREATE TABLE ROLE (
    role_id INT PRIMARY KEY,
    role_name VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE STATUS (
    status_id INT PRIMARY KEY,
    status_name VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE BLOCK_TYPE (
    block_type_id INT PRIMARY KEY,
    type_name VARCHAR(50) UNIQUE NOT NULL
);

-- Insert Default Lookups
INSERT INTO ROLE (role_id, role_name) VALUES 
(1, 'Reviewer'), (2, 'Author'), (3, 'Editor');

INSERT INTO STATUS (status_id, status_name) VALUES 
(1, 'Draft'), (2, 'Pending Editor Review'), (3, 'Needs Improvement'), (4, 'Rejected'), (5, 'Published');

INSERT INTO BLOCK_TYPE (block_type_id, type_name) VALUES 
(1, 'Text'), (2, 'Heading'), (3, 'Code'), (4, 'Image');
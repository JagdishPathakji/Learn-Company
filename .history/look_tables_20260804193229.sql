-- database name
CREATE DATABASE knowledge_base;

-- refering to this database for next set of sql statements
USE knowledge_base;

-- this table is for the different roles provided like (author, editor, reviewer / normal user)
CREATE TABLE ROLE (
    role_id INT PRIMARY KEY,
    role_name VARCHAR(50) UNIQUE NOT NULL
);

-- this table is to keep the track of status (draft -> pending for review -> needs improvement / rejected / published)
CREATE TABLE STATUS (
    status_id INT PRIMARY KEY,
    status_name VARCHAR(50) UNIQUE NOT NULL
);

-- this table is for the type of content we will allow in articles (text, code, image)
CREATE TABLE BLOCK_TYPE (
    block_type_id INT PRIMARY KEY,
    type_name VARCHAR(50) UNIQUE NOT NULL
);

-- different categories 
CREATE TABLE CATEGORY (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL
);


-- Insert Default values in all lookup tables
INSERT INTO ROLE (role_id, role_name) VALUES 
(1, 'Reviewer'), (2, 'Author'), (3, 'Editor');

INSERT INTO STATUS (status_id, status_name) VALUES 
(1, 'Draft'), (2, 'Pending Editor Review'), (3, 'Needs Improvement'), (4, 'Rejected'), (5, 'Published');

INSERT INTO BLOCK_TYPE (block_type_id, type_name) VALUES 
(1, 'Text'), (3, 'Code'), (4, 'Image');

INSERT INTO CATEGORY (name) VALUES 
('Engineering & Technology'),
('Product & Design'),
('Human Resources'),
('Sales & Marketing'),
('Customer Support'),
('Company Operations');
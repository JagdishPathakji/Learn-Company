USE knowledge_base;

-- DDL (CREATE, ALTER, DROP)
-- CREATE used previously to create schema



-- ALTER
-- Adding a column to USER table
ALTER TABLE USER ADD COLUMN bio TEXT NULL;

-- Allow Floating point ratings in USER_RATING table
-- M (Precision) = Total number of digits (before + after the decimal point)
-- D (Scale) = Number of digits after the decimal point
ALTER TABLE USER_RATING MODIFY COLUMN rating_value DECIMAL(2,1) NOT NULL;

-- Adding Sample Indexing 
ALTER TABLE ARTICLE_VERSION ADD INDEX idx_article_title (title);



-- DROP
-- Droping the above Sample Index
ALTER TABLE ARTICLE_VERSION DROP INDEX idx_article_title;

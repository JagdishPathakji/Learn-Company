USE knowledge_base;

-- setting up UUID manually for now
SET @author_id  = UUID_TO_BIN('11111111-1111-1111-1111-111111111111', 1);
SET @editor_id  = UUID_TO_BIN('22222222-2222-2222-2222-222222222222', 1);
SET @reviewer_id  = UUID_TO_BIN('33333333-3333-3333-3333-333333333333', 1);

-- INSERT MANY ROWS AT A TIME (USERS)
INSERT INTO USER (user_id, username, email, password_hash) VALUES 
(@author_id , 'jagdish', 'jagdish@example.com', 'hash1'),
(@editor_id , 'mihir', 'mihir@example.com', 'hash2'),
(@reviewer_id , 'rudra', 'rudra@example.com', 'hash3');

-- ASSIGN ROLES TO USERS FIRST!
INSERT INTO USER_ROLE (user_id, role_id) VALUES (@author_id, 2); -- Author
INSERT INTO USER_ROLE (user_id, role_id) VALUES (@editor_id, 3); -- Editor
INSERT INTO USER_ROLE (user_id, role_id) VALUES (@reviewer_id, 1); -- Reviewer

-- ==========================================
-- ARTICLE 1
-- ==========================================
SET @article_id = UUID_TO_BIN('AAAAAAAA-AAAA-AAAA-AAAA-AAAAAAAAAAAA', 1);
INSERT INTO ARTICLE (article_id, author_id) VALUES (@article_id, @author_id);

SET @version_id = UUID_TO_BIN('BBBBBBBB-BBBB-BBBB-BBBB-BBBBBBBBBBBB', 1);
INSERT INTO ARTICLE_VERSION (version_id, article_id, version_number, title, status_id, created_by)
VALUES (@version_id, @article_id, 1, 'My Awesome SQL Guide', 2, @author_id);

INSERT INTO CONTENT_BLOCK (version_id, block_type_id, content_data, sequence_order) VALUES
(@version_id, 1, 'SQL stands for Structured Query Language.', 1),
(@version_id, 3, 'SELECT * FROM users;', 2);

-- ==========================================
-- ARTICLE 2
-- ==========================================
SET @article2_id = UUID_TO_BIN('CCCCCCCC-CCCC-CCCC-CCCC-CCCCCCCCCCCC', 1);
INSERT INTO ARTICLE (article_id, author_id) VALUES (@article2_id, @author_id);

SET @version2_id = UUID_TO_BIN('DDDDDDDD-DDDD-DDDD-DDDD-DDDDDDDDDDDD', 1);
INSERT INTO ARTICLE_VERSION (version_id, article_id, version_number, title, status_id, created_by)
VALUES (@version2_id, @article2_id, 1, 'Advanced Joins Explained', 1, @author_id);

INSERT INTO CONTENT_BLOCK (version_id, block_type_id, content_data, sequence_order) VALUES
(@version2_id, 1, 'A LEFT JOIN returns all records from the left table, and the matched records from the right table.', 1),
(@version2_id, 3, 'SELECT a.title, u.username FROM ARTICLE_VERSION a LEFT JOIN USER u ON a.created_by = u.user_id;', 2);

-- ==========================================
-- ARTICLE 3
-- ==========================================
SET @article3_id = UUID_TO_BIN('EEEEEEEE-EEEE-EEEE-EEEE-EEEEEEEEEEEE', 1);
INSERT INTO ARTICLE (article_id, author_id) VALUES (@article3_id, @author_id);

SET @version3_id = UUID_TO_BIN('FFFFFFFF-FFFF-FFFF-FFFF-FFFFFFFFFFFF', 1);
INSERT INTO ARTICLE_VERSION (version_id, article_id, version_number, title, status_id, created_by)
VALUES (@version3_id, @article3_id, 1, 'Database Normalization', 1, @author_id);

INSERT INTO CONTENT_BLOCK (version_id, block_type_id, content_data, sequence_order) VALUES
(@version3_id, 1, 'Normalization reduces data redundancy and improves data integrity.', 1),
(@version3_id, 1, 'First Normal Form (1NF) requires that all columns contain atomic, indivisible values.', 2);
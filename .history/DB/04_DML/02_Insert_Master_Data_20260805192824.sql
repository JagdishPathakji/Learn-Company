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

-- INSERT ARTICLE
SET @article_id = UUID_TO_BIN('AAAAAAAA-AAAA-AAAA-AAAA-AAAAAAAAAAAA', 1);
INSERT INTO ARTICLE (article_id, author_id) VALUES (@article_id, @author_id);

-- ATTACH A VERSION
SET @version_id = UUID_TO_BIN('BBBBBBBB-BBBB-BBBB-BBBB-BBBBBBBBBBBB', 1);
INSERT INTO ARTICLE_VERSION (version_id, article_id, version_number, title, status_id, created_by)
VALUES (@version_id, @article_id, 1, 'My Awesome SQL Guide', 1, @author_id);

-- ATTACH CONTENT
INSERT INTO CONTENT_BLOCK (version_id, block_type_id, content_data, sequence_order) VALUES
(@version_id, 1, 'SQL stands for Structured Query Language.', 1),
(@version_id, 3, 'SELECT * FROM users;', 2);



-- Ensure variables are set for the session
SET @article_id = UUID_TO_BIN('AAAAAAAA-AAAA-AAAA-AAAA-AAAAAAAAAAAA', 1);
SET @version_id = UUID_TO_BIN('BBBBBBBB-BBBB-BBBB-BBBB-BBBBBBBBBBBB', 1);
SET @editor_id  = UUID_TO_BIN('22222222-2222-2222-2222-222222222222', 1);
SET @reviewer_id  = UUID_TO_BIN('33333333-3333-3333-3333-333333333333', 1);

-- ATTACH CATEGORIES
INSERT IGNORE INTO ARTICLE_CATEGORY (article_id, category_id) VALUES (@article_id, 1);

-- Editor Reviews Article
INSERT INTO EDITORIAL_REVIEW (version_id, editor_id, decision, feedback)
VALUES (@version_id, @editor_id, 'Approve', 'Excellent tutorial. Ready to go live!');

-- User Rates Article
INSERT IGNORE INTO USER_RATING (article_id, user_id, rating_value) 
VALUES (@article_id, @reviewer_id, 5);

-- User Comments on Article
INSERT INTO USER_COMMENT (article_id, user_id, comment_text) 
VALUES (@article_id, @reviewer_id, 'This guide saved my life today, thank you Jagdish!');

-- 1. setting up UUID manually for now
-- 1 changes UUID in such a way to have timestamp based sorted order (helps in searching)
SET @user1_id = UUID_TO_BIN('11111111-1111-1111-1111-111111111111', 1);
SET @user2_id = UUID_TO_BIN('22222222-2222-2222-2222-222222222222', 1);
SET @user3_id = UUID_TO_BIN('33333333-3333-3333-3333-333333333333', 1);


-- 2. INSERT MANY ROWS AT A TIME
INSERT INTO USER (user_id, username, email, password_hash) VALUES 
(@user1_id, 'jagdish', 'jagdish@example.com', 'hash1'),
(@user2_id, 'mihir', 'mihir@example.com', 'hash2'),
(@user3_id, 'rudra', 'rudra@example.com', 'hash3');


-- 3. INSERT BASED ON SELECT
INSERT INTO USER_ROLE (user_id,role_id) 
SELECT user_id, 2 FROM USER WHERE username = 'jagdish'; -- setting as author

INSERT INTO USER_ROLE (user_id,role_id)
SELECT user_id, 3 FROM USER WHERE username = 'mihir'; -- setting as editor

INSERT INTO USER_ROLE (user_id,role_id)
SELECT user_id, 1 FROM USER WHERE username = 'rudra'; -- setting as reviewer


-- 4. INSERT A ARTICLE
SET @article_id = UUID_TO_BIN('AAAAAAAA-AAAA-AAAA-AAAA-AAAAAAAAAAAA', 1);
-- The article is born (but has no published version yet)
INSERT INTO ARTICLE (article_id, author_id) VALUES (@article_id, @author_id);


-- 5. ATTACH A VERSION FIRST
SET @version_id = UUID_TO_BIN('BBBBBBBB-BBBB-BBBB-BBBB-BBBBBBBBBBBB', 1);
-- The Author saves their first Draft (Status 1 = Draft)
INSERT INTO ARTICLE_VERSION (version_id, article_id, version_number, title, status_id, created_by)
VALUES (@version_id, @article_id, 1, 'My Awesome SQL Guide', 1, @author_id);


-- 6. ATTACH CONTENT TO THIS VERSION
INSERT INTO CONTENT_BLOCK (version_id, block_type_id, content_data, sequence_order) VALUES
(@version_id, 1, 'SQL stands for Structured Query Language.', 1),
(@version_id, 3, 'SELECT * FROM users;', 2);


-- 7. Finally, attach the tags and categories the user selected
INSERT INTO ARTICLE_CATEGORY (article_id, category_id) VALUES (@article_id, 1);
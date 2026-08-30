-- 1. setting up UUID manually for now
-- 1 changes UUID in such a way to have timestamp based sorted order (helps in searching)
SET @author_id  = UUID_TO_BIN('11111111-1111-1111-1111-111111111111', 1);
SET @editor_id  = UUID_TO_BIN('22222222-2222-2222-2222-222222222222', 1);
SET @reviewer_id  = UUID_TO_BIN('33333333-3333-3333-3333-333333333333', 1);


-- 2. INSERT MANY ROWS AT A TIME
INSERT INTO USER (user_id, username, email, password_hash) VALUES 
(@author_id , 'jagdish', 'jagdish@example.com', 'hash1'),
(@editor_id , 'mihir', 'mihir@example.com', 'hash2'),
(@reviewer_id , 'rudra', 'rudra@example.com', 'hash3');


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


-- 7. ATTACH TAGS AND CATEGORIES
INSERT INTO ARTICLE_CATEGORY (article_id, category_id) VALUES (@article_id, 1);
INSERT INTO TAG (name) VALUES ('SQL');


-- 8. Author clicks "Submit for Review". Backend updates status.
UPDATE ARTICLE_VERSION 
SET status_id = 2 -- Status 2 = Pending Editor Review
WHERE version_id = @version_id;

-- 9. Editor (Mihir) reads the article and clicks "Approve".
-- Backend saves the review...
INSERT INTO EDITORIAL_REVIEW (version_id, editor_id, decision, feedback)
VALUES (@version_id, @editor_id, 'Approve', 'Excellent tutorial. Ready to go live!');
-- ...and Backend instantly upgrades the status to Published.
UPDATE ARTICLE_VERSION 
SET status_id = 5 -- Status 5 = Published
WHERE version_id = @version_id;
-- Backend officially maps this published version to the main article for fast reading.
UPDATE ARTICLE 
SET current_published_version_id = @version_id
WHERE article_id = @article_id;


-- 10. A reviewer (Rudra) reads the now-published article and leaves a 5-star rating and comment.
INSERT INTO USER_RATING (article_id, user_id, rating_value) 
VALUES (@article_id, @reviewer_id, 5);
INSERT INTO USER_COMMENT (article_id, user_id, comment_text) 
VALUES (@article_id, @reviewer_id, 'This guide saved my life today, thank you Jagdish!');
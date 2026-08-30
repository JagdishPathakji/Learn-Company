USE knowledge_base;

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

-- setting up UUID manually for now
-- 1 changes UUID in such a way to have timestamp based sorted order (helps in searching)
SET @user1_id = UUID_TO_BIN('11111111-1111-1111-1111-111111111111', 1);
SET @user2_id = UUID_TO_BIN('22222222-2222-2222-2222-222222222222', 1);
SET @user3_id = UUID_TO_BIN('33333333-3333-3333-3333-333333333333', 1);


-- INSERT VARIATIONS

-- 1. INSERT MANY ROWS AT A TIME
INSERT INTO USER (user_id, username, email, password_hash) VALUES 
(@user1_id, 'jagdish', 'jagdish@example.com', 'hash1'),
(@user2_id, 'mihir', 'mihir@example.com', 'hash2'),
(@user3_id, 'rudra', 'rudra@example.com', 'hash3');


-- 2. INSERT BASED ON SELECT
INSERT INTO USER_ROLE (user_id,role_id) 
SELECT user_id, 2 FROM USER WHERE username = 'jagdish'; -- setting as author

INSERT INTO USER_ROLE (user_id,role_id)
SELECT user_id, 3 FROM USER WHERE username = 'mihir'; -- setting as editor

INSERT INTO USER_ROLE (user_id,role_id)
SELECT user_id, 1 FROM USER WHERE username = 'rudra'; -- setting as reviewer


-- 3. INSERT A ARTICLE
SET @article1_id = UUID_TO_BIN('AAAAAAAA-AAAA-AAAA-AAAA-AAAAAAAAAAAA', 1);

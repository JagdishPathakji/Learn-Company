-- setting up UUID manually for now
-- 1 changes UUID in such a way to have timestamp based sorted order (helps in searching)
SET @user1_id = UUID_TO_BIN('11111111-1111-1111-1111-111111111111', 1);
SET @user2_id = UUID_TO_BIN('22222222-2222-2222-2222-222222222222', 1);
SET @editor_id = UUID_TO_BIN('33333333-3333-3333-3333-333333333333', 1);


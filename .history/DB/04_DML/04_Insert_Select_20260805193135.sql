USE knowledge_base;

-- INSERT BASED ON SELECT (Tags and related mappings)

-- INSERT SELECT for tags
SET @article_id = UUID_TO_BIN('AAAAAAAA-AAAA-AAAA-AAAA-AAAAAAAAAAAA', 1);
INSERT IGNORE INTO TAG (name) VALUES ('SQL');
INSERT IGNORE INTO ARTICLE_TAG (article_id, tag_id) 
SELECT @article_id, tag_id FROM TAG WHERE name = 'SQL';
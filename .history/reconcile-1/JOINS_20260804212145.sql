-- 1. Show Tags for an Article
SELECT 
    t.name AS tag_name
FROM ARTICLE a
-- Join the mapping table
INNER JOIN ARTICLE_TAG at ON a.article_id = at.article_id
-- Join the lookup table to get the actual tag text
INNER JOIN TAG t ON at.tag_id = t.tag_id
WHERE a.article_id = UUID_TO_BIN('AAAAAAAA-AAAA-AAAA-AAAA-AAAAAAAAAAAA', 1);


-- 2. Show Categories for an Article
SELECT
    c.name AS category
FROM ARTICLE a
INNER JOIN ARTICLE_CATEGORY ac ON a.article_id = ac.article_id
INNER JOIN category c ON c.category_id = ac.category_id
WHERE a.article_id = UUID_TO_BIN('AAAAAAAA-AAAA-AAAA-AAAA-AAAAAAAAAAAA', 1);

-- 3. A list of every single user in the database, and the titles of all the officially published articles they have written.

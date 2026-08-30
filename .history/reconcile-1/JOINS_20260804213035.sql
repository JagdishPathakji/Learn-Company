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
SELECT 
    u.username, 
    IFNULL(v.title, 'No Published Articles Yet') AS authored_article_title
FROM USER u 
-- 1. LEFT JOIN to find their articles (if any)
LEFT JOIN ARTICLE a ON u.user_id = a.author_id
-- 2. LEFT JOIN to get the human-readable title of that article
LEFT JOIN ARTICLE_VERSION v ON a.current_published_version_id = v.version_id;


-- 4. Find Unused Categories
SELECT
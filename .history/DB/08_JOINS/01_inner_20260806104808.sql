-- 1. Get Published Articles and their Author's Name
SELECT 
    a.article_id,
    av.title AS article_title,
    u.username AS author_name,
    a.created_at AS original_creation_date
FROM ARTICLE a
INNER JOIN USER u ON a.author_id = u.user_id
INNER JOIN ARTICLE_VERSION av ON a.current_published_version_id = av.version_id;


-- 2. Show Tags for an Article
SELECT 
    t.name AS tag_name
FROM ARTICLE a
INNER JOIN ARTICLE_TAG at ON a.article_id = at.article_id
INNER JOIN TAG t ON at.tag_id = t.tag_id
WHERE a.article_id = UUID_TO_BIN('AAAAAAAA-AAAA-AAAA-AAAA-AAAAAAAAAAAA', 1);



-- 3. Show Categories for an Article
SELECT
    c.name AS category
FROM ARTICLE a
INNER JOIN ARTICLE_CATEGORY ac ON a.article_id = ac.article_id
INNER JOIN CATEGORY c ON c.category_id = ac.category_id
WHERE a.article_id = UUID_TO_BIN('AAAAAAAA-AAAA-AAAA-AAAA-AAAAAAAAAAAA', 1);

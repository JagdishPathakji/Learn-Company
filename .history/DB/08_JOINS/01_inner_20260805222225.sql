-- 1. Get Published Articles and their Author's Name
SELECT 
    a.article_id,
    av.title AS article_title,
    u.username AS author_name,
    a.created_at AS original_creation_date
FROM ARTICLE a
INNER JOIN USER u ON a.author_id = u.user_id
INNER JOIN ARTICLE_VERSION av ON a.current_published_version_id = av.version_id;



SELECT 
    v.title AS article_title,
    GROUP_CONCAT(c.name SEPARATOR ', ') AS categories
FROM ARTICLE a
INNER JOIN ARTICLE_VERSION v ON a.current_published_version_id = v.version_id
INNER JOIN ARTICLE_CATEGORY ac ON a.article_id = ac.article_id
INNER JOIN CATEGORY c ON ac.category_id = c.category_id
WHERE a.article_id = UUID_TO_BIN('AAAAAAAA-AAAA-AAAA-AAAA-AAAAAAAAAAAA', 1);
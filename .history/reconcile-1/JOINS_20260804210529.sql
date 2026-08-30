SELECT 
    v.title AS article_title,
    c.name AS category_name
FROM ARTICLE a
-- Join to get the published version's title
INNER JOIN ARTICLE_VERSION v ON a.current_published_version_id = v.version_id
-- Join the mapping table
INNER JOIN ARTICLE_CATEGORY ac ON a.article_id = ac.article_id
-- Join the lookup table to get the actual category name
INNER JOIN CATEGORY c ON ac.category_id = c.category_id
WHERE a.article_id = UUID_TO_BIN('AAAAAAAA-AAAA-AAAA-AAAA-AAAAAAAAAAAA', 1);
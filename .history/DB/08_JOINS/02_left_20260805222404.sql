-- 2. List All Articles and their Assigned Categories (Including uncategorized articles)
SELECT 
    a.article_id,
    c.name AS category_name
FROM ARTICLE a
LEFT JOIN ARTICLE_CATEGORY ac ON a.article_id = ac.article_id
LEFT JOIN CATEGORY c ON ac.category_id = c.category_id;
-- 1. List All Articles and their Assigned Categories (Including uncategorized articles)
SELECT 
    a.article_id,
    IFNULL(GROUP_CONCAT(c.name SEPARATOR ', '), 'Uncategorized') AS category_names
FROM ARTICLE a
LEFT JOIN ARTICLE_CATEGORY ac ON a.article_id = ac.article_id
LEFT JOIN CATEGORY c ON ac.category_id = c.category_id
GROUP BY a.article_id;
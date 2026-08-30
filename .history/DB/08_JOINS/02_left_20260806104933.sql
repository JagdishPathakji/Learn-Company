-- 1. List All Articles and their Assigned Categories (Including uncategorized articles)
SELECT 
    a.article_id,
    IFNULL(GROUP_CONCAT(c.name SEPARATOR ', '), 'Uncategorized') AS category_names
FROM ARTICLE a
LEFT JOIN ARTICLE_CATEGORY ac ON a.article_id = ac.article_id
LEFT JOIN CATEGORY c ON ac.category_id = c.category_id
GROUP BY a.article_id;


-- 2. A list of every single user in the database, and the titles of all the officially published articles they have written.
SELECT 
    u.username, 
    IFNULL(v.title, 'No Published Articles Yet') AS authored_article_title
FROM USER u 
-- 1. LEFT JOIN to find their articles (if any)
LEFT JOIN ARTICLE a ON u.user_id = a.author_id
-- 2. LEFT JOIN to get the human-readable title of that article
LEFT JOIN ARTICLE_VERSION v ON a.current_published_version_id = v.version_id;

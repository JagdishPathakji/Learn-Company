-- find which user is allocated which role, and find roles which have no user
SELECT 
    ur.user_id, 
    r.role_name AS role_name
FROM USER_ROLE ur
RIGHT JOIN ROLE r ON ur.role_id = r.role_id;

-- 4. Find Unused Categories
SELECT
    c.name AS unused_categories
FROM ARTICLE_CATEGORY ac 
RIGHT JOIN
CATEGORY c ON c.category_id = ac.category_id
WHERE ac.article_id IS NULL;

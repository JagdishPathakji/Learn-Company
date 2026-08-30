-- 
SELECT 
    ur.user_id, 
    r.name AS role_name
FROM USER_ROLE ur
RIGHT JOIN ROLE r ON ur.role_id = r.role_id;
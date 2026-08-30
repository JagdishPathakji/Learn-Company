-- find which user is allocated which role, and find roles which have no user
SELECT 
    ur.user_id, 
    r.name AS role_name
FROM USER_ROLE ur
RIGHT JOIN ROLE r ON ur.role_id = r.role_id;
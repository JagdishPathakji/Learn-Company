-- All details of author like (name, article with its content)

SELECT 

FROM USER u
INNER JOIN USER_ROLE ur ON u.user_id  = ur.user_id
INNER JOIN ROLE r ON ur.role_id = r.role_id AND r.role
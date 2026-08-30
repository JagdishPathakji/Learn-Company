-- SELECT
SELECT username, email FROM USER;

-- SELECT + WHERE
SELECT email FROM USER WHERE username = 'jagdish';

-- SELECT + ORDER BY (New -> Old)
SELECT title, created_at FROM ARTICLE_VERSION ORDER BY created_at DESC;

-- SELECT + ORDER BY + LIMIT (first two users)
SELECT username FROM USER ORDER BY created_at ASC LIMIT 2;

-- SELECT + WHERE + ORDER BY + LIMIT (Published articles , new -> old, latest)
SELECT title FROM ARTICLE_VERSION WHERE status_id = 5 ORDER BY created_at DESC LIMIT 1;

-- SELECT + GROUP BY (Count number of ratings for each article)
SELECT BIN_TO_UUID(article_id,1) AS article_id, COUNT(rating_value) AS total_ratings
FROM USER_RATING GROUP BY article_id;

-- SELECT + GROUP BY + HAVING (Show average of articles having average more than 4.0)
SELECT BIN_TO_UUID(article_id,1) AS article_id, AVG(rating_value) AS average_score
FROM USER_RATING GROUP BY article_id HAVING AVG(rating_value) > 4.0;

-- SELECT + WHERE + GROUP BY + HAVING + ORDER BY + LIMIT ()
SELECT BIN_TO_UUID(articles,1) AS article_id, AVG(rating_value) AS average_score 
FROM USER_RATING
WHERE updated_at >= '2026-01-01 00:00:00'
GROUP BY article_id
HAVING AVG(rating_value) < 3.0
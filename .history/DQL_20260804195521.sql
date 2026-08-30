-- SELECT
SELECT username, email FROM USER;

-- SELECT + WHERE
SELECT email FROM USER WHERE username = 'jagdish';

-- SELECT + ORDER BY (New -> Old)
SELECT title, created_at FROM ARTICLE_VERSION ORDER BY created_at DESC;

-- SELECT + ORDER BY + LIMIT (first two users)
SELECT username FROM USER ORDER BY created_at ASC LIMIT 2;

-- SELECT + WHERE + ORDER BY + LIMIT (Published articles , new -> old, latest)

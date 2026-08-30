-- What it is: The word "Upsert" is a mashup of UPdate and inSERT. It tells the database: "Try to INSERT this row. If the row already exists (based on a Primary Key or Unique Constraint), don't crash! Just UPDATE it instead."

INSERT INTO USER_RATING (article_id, user_id, rating_value) 
VALUES (@article1_id, @reviewer_id, 4)
-- ...but if Rudra already rated this article, just update his existing score!
ON DUPLICATE KEY UPDATE rating_value = 4;
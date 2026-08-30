-- stores user rating for particular article 
CREATE TABLE USER_RATING (
    article_id BINARY(16), -- for which article rating is for
    user_id BINARY(16), -- who has rated
    rating_value TINYINT NOT NULL CHECK (rating_value >= 1 AND rating_value <= 5), -- rated value
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- when 
    PRIMARY KEY (article_id, user_id),
    FOREIGN KEY (article_id) REFERENCES ARTICLE(article_id) ON DELETE CASCADE, -- delete this entry if article is deleted
    FOREIGN KEY (user_id) REFERENCES USER(user_id) ON DELETE CASCADE -- delete this entry if the user (reviewer) is deleted
);

-- stores user comments for article
CREATE TABLE USER_COMMENT (
    comment_id BINARY(16) DEFAULT (UUID_TO_BIN(UUID(), 1)) PRIMARY KEY,
    article_id BINARY(16) NOT NULL, -- for which article comment is for
    user_id BINARY(16) NOT NULL, -- 
    comment_text TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (article_id) REFERENCES ARTICLE(article_id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES USER(user_id) ON DELETE CASCADE
);
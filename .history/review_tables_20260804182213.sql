-- stores user rating for particular article 
CREATE TABLE USER_RATING (
    article_id BINARY(16), -- unique rating
    user_id BINARY(16), -- who has rated
    rating_value TINYINT NOT NULL CHECK (rating_value >= 1 AND rating_value <= 5), -- rated value
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (article_id, user_id),
    FOREIGN KEY (article_id) REFERENCES ARTICLE(article_id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES USER(user_id) ON DELETE CASCADE
);

CREATE TABLE USER_COMMENT (
    comment_id BINARY(16) DEFAULT (UUID_TO_BIN(UUID(), 1)) PRIMARY KEY,
    article_id BINARY(16) NOT NULL,
    user_id BINARY(16) NOT NULL,
    comment_text TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (article_id) REFERENCES ARTICLE(article_id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES USER(user_id) ON DELETE CASCADE
);
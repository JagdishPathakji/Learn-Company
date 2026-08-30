-- storing track of 
CREATE TABLE EDITORIAL_REVIEW (
    review_id BINARY(16) DEFAULT (UUID_TO_BIN(UUID(), 1)) PRIMARY KEY,
    version_id BINARY(16) NOT NULL,
    editor_id BINARY(16) NOT NULL,
    decision ENUM('Approve', 'Reject', 'Suggest Improvements') NOT NULL,
    feedback TEXT NOT NULL,
    reviewed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (version_id) REFERENCES ARTICLE_VERSION(version_id) ON DELETE CASCADE,
    FOREIGN KEY (editor_id) REFERENCES USER(user_id)
);

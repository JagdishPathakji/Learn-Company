-- 2. USERS & ROLES
-- ------------------------------------------------------------------------------
CREATE TABLE USER (
    user_id BINARY(16) DEFAULT (UUID_TO_BIN(UUID(), 1)) PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE USER_ROLE (
    user_id BINARY(16),
    role_id INT,
    PRIMARY KEY (user_id, role_id),
    FOREIGN KEY (user_id) REFERENCES USER(user_id) ON DELETE CASCADE,
    FOREIGN KEY (role_id) REFERENCES ROLE(role_id) ON DELETE CASCADE
);


-- 3. ARTICLE ORGANIZATION
-- ------------------------------------------------------------------------------
CREATE TABLE CATEGORY (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE TAG (
    tag_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE ARTICLE (
    article_id BINARY(16) DEFAULT (UUID_TO_BIN(UUID(), 1)) PRIMARY KEY,
    author_id BINARY(16) NOT NULL,
    current_published_version_id BINARY(16) NULL, -- Will be set via foreign key after ARTICLE_VERSION is created
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (author_id) REFERENCES USER(user_id)
);

CREATE TABLE ARTICLE_CATEGORY (
    article_id BINARY(16),
    category_id INT,
    PRIMARY KEY (article_id, category_id),
    FOREIGN KEY (article_id) REFERENCES ARTICLE(article_id) ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES CATEGORY(category_id) ON DELETE CASCADE
);

CREATE TABLE ARTICLE_TAG (
    article_id BINARY(16),
    tag_id INT,
    PRIMARY KEY (article_id, tag_id),
    FOREIGN KEY (article_id) REFERENCES ARTICLE(article_id) ON DELETE CASCADE,
    FOREIGN KEY (tag_id) REFERENCES TAG(tag_id) ON DELETE CASCADE
);


-- 4. VERSIONING & NORMALIZED CONTENT
-- ------------------------------------------------------------------------------
CREATE TABLE ARTICLE_VERSION (
    version_id BINARY(16) DEFAULT (UUID_TO_BIN(UUID(), 1)) PRIMARY KEY,
    article_id BINARY(16) NOT NULL,
    version_number INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    status_id INT NOT NULL,
    created_by BINARY(16) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (article_id) REFERENCES ARTICLE(article_id) ON DELETE CASCADE,
    FOREIGN KEY (status_id) REFERENCES STATUS(status_id),
    FOREIGN KEY (created_by) REFERENCES USER(user_id)
);

-- Add the circular foreign key for the Read Optimization on ARTICLE
ALTER TABLE ARTICLE 
ADD CONSTRAINT fk_current_published_version 
FOREIGN KEY (current_published_version_id) REFERENCES ARTICLE_VERSION(version_id) ON DELETE SET NULL;

CREATE TABLE CONTENT_BLOCK (
    block_id BINARY(16) DEFAULT (UUID_TO_BIN(UUID(), 1)) PRIMARY KEY,
    version_id BINARY(16) NOT NULL,
    block_type_id INT NOT NULL,
    content_data TEXT,
    sequence_order INT NOT NULL,
    FOREIGN KEY (version_id) REFERENCES ARTICLE_VERSION(version_id) ON DELETE CASCADE,
    FOREIGN KEY (block_type_id) REFERENCES BLOCK_TYPE(block_type_id)
);


-- 5. EDITORIAL WORKFLOW
-- ------------------------------------------------------------------------------
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


-- 6. ENGAGEMENT (Normal Users / Reviewers)
-- ------------------------------------------------------------------------------
CREATE TABLE USER_RATING (
    article_id BINARY(16),
    user_id BINARY(16),
    rating_value TINYINT NOT NULL CHECK (rating_value >= 1 AND rating_value <= 5),
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
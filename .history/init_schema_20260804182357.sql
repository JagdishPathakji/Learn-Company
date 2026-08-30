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



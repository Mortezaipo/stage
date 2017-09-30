/**
 * stage database structure
 */

CREATE TABLE IF NOT EXISTS users (
    user_id        serial          PRIMARY KEY,
    email          varchar(50)     NOT NULL CONSTRAINT true_email CHECK (email ~* '^[a-z0-9\-\_\.]+@[a-z0-9\.\_]+\.[a-z]{1,}$') UNIQUE,
    password       varchar(64)     NOT NULL,
    is_locked      boolean         DEFAULT false,
    first_login    timestamp       NULL,
    last_login     timestamp       NULL,
    permission     char(3)         DEFAULT "777",
    created        timestamp       DEFAULT now(),
    modified       timestamp       NULL
);

CREATE TABLE IF NOT EXISTS pages (
    page_id        serial          PRIMARY KEY,
    title          varchar(200)    NOT NULL UNIQUE,
    body           text            NOT NULL,
    views          integer         DEFAULT 0,
    show_menu      boolean         DEFAULT true,
    priority       integer         DEFAULT 0,
    created        timestamp       DEFAULT now(),
    modified       timestamp       NULL
);

CREATE TABLE IF NOT EXISTS posts (
    post_id        serial          PRIMARY KEY,
    admin_id       integer         NOT NULL REFERENCES users(user_id),
    title          varchar(100)    NOT NULL UNIQUE,
    description    text            NOT NULL,
    body           text            NOT NULL,
    views          integer         DEFAULT 0,
    priority       integer         DEFAULT 0,
    created        timestamp       DEFAULT now(),
    modified       timestamp       NULL
);

CREATE TABLE IF NOT EXISTS projects (
    project_id     serial          PRIMARY KEY,
    admin_id       integer         NOT NULL REFERENCES users(user_id),
    name           varchar(30)     NOT NULL,
    description    varchar(100)    NOT NULL,
    body           text            NOT NULL,
    views          integer         DEFAULT 0,
    tags           varchar(20)[]   NOT NULL, 
    images         integer[9]      NOT NULL,
    priority       integer         DEFAULT 0,
    created        timestamp       DEFAULT now(),
    modified       timestamp       NULL
);

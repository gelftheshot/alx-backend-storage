-- script that creates a stored procedure AddBonus that adds a new correction for a student
DELIMITER $$
CREATE PROCEDURE AddBonus (IN user_id INT, IN project_name VARCHAR(255), IN score FLOAT)
BEGIN
    CREATE TABLE IF NOT EXISTS projects (
        id INT NOT NULL AUTO_INCREMENT,
        name VARCHAR(255) NOT NULL,
        PRIMARY KEY (id),
        UNIQUE KEY (name)
    );

    INSERT INTO projects (name) VALUES (project_name)
    ON DUPLICATE KEY UPDATE name = name;

    INSERT INTO corrections (user_id, project_id, score)
    VALUES (
        user_id,
        (SELECT id FROM projects WHERE name = project_name),
        score
    );
END$$
DELIMITER ;

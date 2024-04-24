-- avrage of the score of each projects
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id FLOAT)
BEGIN
    UPDATE users
    SET average_score = (SELECT AVG(c.score) FROM corrections c WHERE c.user_id = user_id)
    WHERE id = user_id;
END$$
DELIMITER ;

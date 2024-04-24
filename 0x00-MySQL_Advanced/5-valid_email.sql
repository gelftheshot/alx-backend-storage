-- change the valid email value when email changed
DELIMITER //

CREATE TRIGGER email_trigger
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email <> OLD.email THEN
        SET NEW.valid_email = CASE WHEN NEW.valid_email = 1 THEN 0 ELSE 1 END;
    END IF;
END //

DELIMITER ;

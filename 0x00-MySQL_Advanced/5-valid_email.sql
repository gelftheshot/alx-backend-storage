-- change the valid email value when email changed
DELIMITER //

CREATE TRIGGER email_trigger
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email <> OLD.email THEN
        SET NEW.valid_email = CASE WHEN NEW.valid_email = 0;
    END IF;
END //

DELIMITER ;

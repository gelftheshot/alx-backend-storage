-- function for divition and reutn the float value
DELIMITER $$
DROP FUNCTION IF EXISTS SafeDiv;
CREATE FUNCTION SafeDiv(a int, b int)
RETURN FLOAT
BEGIN
	DECLARE result FLOAT;
	IF b = 0 THEN
		SET result = 0;
	ELSE
		SET result = a / b;
	END IF;
	RETURN result;
END;
$$

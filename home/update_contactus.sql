DELIMITER //

CREATE TRIGGER UpdateContactUsResponse
BEFORE UPDATE ON home_contactus
FOR EACH ROW
BEGIN
    IF NEW.response IS NOT NULL THEN
        SET NEW.response_on = NOW();
        SET NEW.closed = 1;
    END IF;
END;

//

DELIMITER ;
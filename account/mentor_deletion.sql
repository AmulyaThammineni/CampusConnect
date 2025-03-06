DELIMITER //

CREATE PROCEDURE RemoveInactiveMentorsSixMonths()
BEGIN
    DECLARE cutoff_date DATETIME;
    SET cutoff_date = NOW() - INTERVAL 180 DAY;
    
    -- Delete mentors who are not approved and have a last_application_date greater than the cutoff date
    DELETE FROM account_mentor
    WHERE approved = 0 AND last_application_date < cutoff_date;
    
END;

//

DELIMITER ;


-- just for demo
DELIMITER //

CREATE PROCEDURE RemoveInactiveMentorsOneDay()
BEGIN
    DECLARE cutoff_date DATETIME;
    SET cutoff_date = NOW() - INTERVAL 1 DAY;
    
    -- Delete mentors who are not approved and have a last_application_date greater than the cutoff date
    DELETE FROM account_mentor
    WHERE approved = 0 AND last_application_date < cutoff_date;
    
END;

//

DELIMITER ;


-- to view procedures for an app
 SELECT SPECIFIC_NAME
 FROM information_schema.ROUTINES
 WHERE ROUTINE_TYPE = 'PROCEDURE'
 AND ROUTINE_SCHEMA = 'collegeconnect';
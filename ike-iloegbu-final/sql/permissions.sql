USE MUSIC_STUDIO;

DROP ROLE IF EXISTS 'read_role';

CREATE ROLE IF NOT EXISTS 'read_role';

GRANT SELECT ON *.* TO 'read_role';

GRANT 'read_role' TO 'read_only'@'%';

SET DEFAULT ROLE 'read_role' TO 'read_only'@'%';

DROP ROLE IF EXISTS 'modify_role';

CREATE ROLE IF NOT EXISTS 'modify_role';

GRANT INSERT, UPDATE, DELETE ON *.* TO 'modify_role';

GRANT 'modify_role' TO 'modify_user'@'%';

SET DEFAULT ROLE 'modify_role' TO 'modify_user'@'%';

DROP ROLE IF EXISTS 'admin_role';

CREATE ROLE IF NOT EXISTS 'admin_role';

GRANT ALL PRIVILEGES ON *.* TO 'admin_role' WITH GRANT OPTION;

GRANT 'admin_role' TO 'admin_user'@'%';

SET DEFAULT ROLE 'admin_role' TO 'admin_user'@'%';

SHOW GRANTS FOR 'admin_user';

SHOW GRANTS FOR 'modify_user';

SHOW GRANTS FOR 'read_only';

-- MODIFY ROLE
GRANT EXECUTE ON PROCEDURE addClient TO modify_role;
GRANT EXECUTE ON PROCEDURE addEmp TO modify_role;
GRANT EXECUTE ON PROCEDURE calc_month_earnings TO modify_role;
GRANT EXECUTE ON PROCEDURE client_sessions TO modify_role;
GRANT EXECUTE ON PROCEDURE displayClients TO modify_role;
GRANT EXECUTE ON PROCEDURE displayEmployees TO modify_role;
GRANT EXECUTE ON PROCEDURE emp_earnings TO modify_role;
GRANT EXECUTE ON PROCEDURE emp_sessions TO modify_role;
GRANT EXECUTE ON PROCEDURE month_earnings TO modify_role;
GRANT EXECUTE ON PROCEDURE year_earnings TO modify_role;
GRANT EXECUTE ON PROCEDURE book_session TO modify_role;
GRANT EXECUTE ON PROCEDURE addService TO modify_role;
GRANT EXECUTE ON PROCEDURE viewService TO modify_role;
GRANT EXECUTE ON PROCEDURE all_session TO modify_role;



-- READ ROLE

GRANT EXECUTE ON PROCEDURE calc_month_earnings TO read_role;
GRANT EXECUTE ON PROCEDURE client_sessions TO read_role;
GRANT EXECUTE ON PROCEDURE displayClients TO read_role;
GRANT EXECUTE ON PROCEDURE displayEmployees TO read_role;
GRANT EXECUTE ON PROCEDURE emp_earnings TO read_role;
GRANT EXECUTE ON PROCEDURE emp_sessions TO read_role;
GRANT EXECUTE ON PROCEDURE month_earnings TO read_role;
GRANT EXECUTE ON PROCEDURE year_earnings TO read_role;
GRANT EXECUTE ON PROCEDURE all_session TO read_role;
GRANT EXECUTE ON PROCEDURE viewService TO read_role;



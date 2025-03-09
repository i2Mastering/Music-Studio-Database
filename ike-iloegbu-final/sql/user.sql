USE MUSIC_STUDIO;

DROP USER IF EXISTS 'admin_user'@'%';
DROP USER IF EXISTS 'read_only'@'%';
DROP USER IF EXISTS 'modiy_user'@'%';

CREATE USER IF NOT EXISTS 'read_only'@'%' IDENTIFIED BY 'read1234'  ;

CREATE USER IF NOT EXISTS 'modify_user'@'%' IDENTIFIED BY 'modify1234';

CREATE USER IF NOT EXISTS 'admin_user'@'%' IDENTIFIED BY 'admin1234';
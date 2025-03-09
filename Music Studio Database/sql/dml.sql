USE MUSIC_STUDIO;



INSERT INTO EMPLOYEE(EMP_FIRST_NAME, EMP_LAST_NAME, EMP_EMAIL) VALUES
('Ike', 'Iloegbu', 'ike@i2mastering.com'),
('Tony','Maserati','tony@i2mastering.com'),
('Leslie','Brathwaite','leslie@i2mastering.com'),
('Jimmy', 'Douglass','jimmy@i2mastering.com'),
('Dave','Darlington','dave@i2mastering.com');

INSERT INTO CLIENT VALUES
('Mack','Miller','m@miller.com', '54 Penn Ave Coopertown, Washington 59362 USA','404-888-2332'),
('Jay','Z','j@z.com', '1002 Marcy Ave Brooklyn, New York 11221 USA','347-323-0988'),
('Kendrick','Lamar','k@tde.com', '808 Lynn St Compton, California 88403 USA','676-323-4594'),
('Afro','Jack','a@jack.net', '2 Grand Pl Miami, Florida 23321 USA','544-443-2345'),
('Will','Iam','w@iam.com', '254 Martin Luther King Blvd Baltimore, Maryland 87065 USA','760-343-2346'),
('Aubrey','Graham', 'a@graham.com', '111 Lucky Ave New York, New York 11823 USA','347-665-5454'),
('Lil','Wayne','wayne@cashmoneyrecords.com', '505 Hollygrove Ave New Orleans, Louisiana 59362 USA','404-888-2332'),
('Cardi','B','c@b.com','1100 Lennox Ave Bronx, New York 19923 USA','718-234-3244'),
('Rick','Ross','r@rosay.com','10 Collins ave Miami, Florida 65545 USA','303-222-5549'),
('Dua', 'Lipa', 'd@lipa.com', '444 Gray St Los Angeles, California 44342 USA','676-433-8778'),
('Taylor','Swift','t@swift.com', '2 Manhattan Ave Brooklyn, New York 11222 USA','718-854-3332'),
('Post', 'Malone', 'p@malone.com', '989 Harrison st Omaha, Nebraska 45678 USA','254-433-5646')
;

INSERT INTO SERVICES VALUES
('3 Hour Recording Session', 'Short-style recording session', 200.00),
('6 Hour Recording Session', 'Full day recording session', 350.00),
('12 Hour Recording Session', 'Max block-out session', 620.00),
('Lite Mix', '12 or less multi-tracks',275.00),
('Full Mix', '12 or more multi-tracks', 425.00),
('Mastering', 'Finalizing your music production', 125.00)
;

INSERT INTO BOOKING(CLIENT_EMAIL,SERVICE_NAME,EMP_ID,BOOKING_DATE)VALUES
('p@malone.com', '6 Hour Recording Session', 1, '2024-02-12'),
('t@swift.com','Full Mix',1, '2024-02-20'),
('d@lipa.com', 'Mastering', 1, '2024-02-21'),
('r@rosay.com', '3 Hour Recording Session', 2, '2024-03-02'),
('c@b.com', '6 Hour Recording Session',2, '2024-03-05'),
('wayne@cashmoneyrecords.com', 'Mastering', 2, '2024-03-10'),
('a@graham.com', 'Full Mix', 3, '2024-03-20'),
('w@iam.com', 'Lite Mix', 3, '2024-04-10'),
('a@jack.net', '12 Hour Recording Session', 4, '2024-04-20'),
('k@tde.com', '6 Hour Recording Session', 4, '2024-04-25'),
('j@z.com', '12 Hour Recording Session', 5, '2024-05-01'),
('m@miller.com', 'Full Mix', 5, '2024-05-10')
;


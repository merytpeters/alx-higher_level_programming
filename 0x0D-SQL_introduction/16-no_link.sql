-- Add new data and list score and name of table second_table
INSERT INTO second_table (score, name) VALUES (18, 'Aria');
INSERT INTO second_table (score, name) VALUES (12, 'Aria');
SELECT score, name FROM second_table ORDER BY score DESC;

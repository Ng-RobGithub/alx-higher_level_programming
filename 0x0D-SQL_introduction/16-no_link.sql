-- Script lists all records of the table second_table having a name value in my MySQL server.
-- Records are ordered by descending score.
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;

UPDATE klient SET date_of_reg = SUBSTR(date_of_reg, 7, 4) || '-' || SUBSTR(date_of_reg, 4, 2) || '-' || SUBSTR(date_of_reg, 1, 2);
SELECT login FROM klient ORDER BY date_of_reg DESC LIMIT 1;
SELECT DISTINCT(SUBSTR(birthday, 1, 4)) FROM klient;
SELECT COUNT(*) AS 'total_items' FROM tovar;
SELECT AVG(CAST((julianday('now') - julianday(birthday)) AS INTEGER) / 365) FROM klient WHERE (CAST((julianday('now') - julianday(date_of_reg)) AS INTEGER) <= 61);
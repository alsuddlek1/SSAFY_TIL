CREATE TABLE users(
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    country TEXT NOT NULL,
    phone TEXT NOT NULL,
    balance INTEGER NOT NULL
    );

DROP TABLE users;

SELECT first_name,age FROM users;
SELECT * FROM users;
SELECT rowid, first_name FROM users;

SELECT first_name, age FROM users ORDER BY age;
SELECT first_name, age FROM users ORDER BY age DESC;
SELECT first_name, age, balance FROM users ORDER BY age, balance DESC;

SELECT country FROM users;
SELECT DISTINCT country FROM users ORDER BY country;
SELECT DISTINCT first_name, country FROM users ORDER BY country;

SELECT first_name, age, balance FROM users WHERE age >= 30;
SELECT first_name, age, balance FROM users WHERE age >= 30 AND balance > 500000;

SELECT first_name, last_name FROM users WHERE first_name LIKE '%호%';
SELECT first_name FROM users WHERE first_name LIKE '%준';
SELECT phone FROM users WHERE phone LIKE '02-%';
SELECT first_name, age FROM users WHERE age LIKE '2_';
SELECT first_name, phone FROM users WHERE phone LIKE '%-51__-%' ;

SELECT first_name, country FROM users WHERE country IN ('경기도', '강원도');
SELECT first_name, country FROM users WHERE country NOT IN ('경기도', '강원도'); 

SELECT first_name, age FROM users WHERE age BETWEEN 20 and 30;
SELECT first_name, age FROM users WHERE age NOT BETWEEN 20 and 30;

SELECT rowid, first_name FROM users LIMIT 10;
SELECT first_name, balance FROM users ORDER BY balance DESC LIMIT 10;
SELECT first_name, age FROM users ORDER BY age LIMIT 5;
SELECT first_name, age FROM users ORDER BY age LIMIT 10 OFFSET 15;

SELECT COUNT(*) FROM users;
SELECT avg(balance) FROM users;

SELECT DISTINCT country, avg(balance) FROM users GROUP BY country ORDER BY avg(balance) DESC;
SELECT avg(age) FROM users WHERE age >= 30;
SELECT country, count(country) from users GROUP BY country;

SELECT last_name, count(*) FROM users GROUP BY last_name;
SELECT last_name, count(*) FROM users GROUP BY last_name ORDER BY count(*) DESC;
SELECT country, avg(age) FROM users GROUP BY country;

CREATE TABLE classmate(
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    address TEXT NOT NULL
);

INSERT INTO classmate(name, age, address) VALUES ('홍길동', 23, '서울');
INSERT INTO classmate VALUES ('김철수', 30, '경기'), ('이영미', 31, '강원'), ('박진성', 26, '전라'), ('최지수', 12, '충청'), ('정요한', 28, '경상');

UPDATE classmate SET name = '신종혁', age = 27 WHERE rowid = 2;
UPDATE classmate SET name = '신종혁', age = 27, address = '부산(근데 아닌거같음)' WHERE rowid = 2;

DELETE FROM classmate WHERE rowid = 5;
DELETE FROM classmate WHERE name LIKE '%종%';

DELETE FROM classmate;
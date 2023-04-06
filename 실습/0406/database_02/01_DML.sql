-- users table 생성
CREATE TABLE users (
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    country TEXT NOT NULL,
    phone TEXT NOT NULL,
    balance INTEGER NOT NULL
);

SELECT COUNT(*) FROM users;
SELECT avg(balance) FROM users;

SELECT country, avg(balance) FROM users WHERE country='전라북도';
SELECT country, avg(balance) FROM users GROUP BY country ORDER BY avg(balance) DESC;

SELECT avg(age) FROM users WHERE age >= 30;

SELECT last_name, count(*)AS number_of_name FROM users GROUP BY last_name;

CREATE TABLE classmate (
name TEXT NOT NULL,
age INTEGER NOT NULL,
address TEXT NOT NULL
);

-- INSERT INTO classmate (name, age, address) VALUES ('홍길동', 23, '서울');
INSERT INTO classmate VALUES('홍길동', 23, '서울');

INSERT INTO classmate VALUES('김철수', 30, '경기'), ('이영미', 31, '강원'), ('박진성', 26, '전라'), ('최지수', 12, '충청'), ('정요한',28, '경상');

--인됨
UPDATE classmate SET name='김철수한무두루미', address='제주도' WHERE rowid=2;

-- 이ㅔㅈ는 이게안됨
DELETE FROM classmate WHERE rowid=5;
DELETE FROM classmate WHERE name LIKE '%영%';
DELETE FROM classmate;

SELECT rowid, * FROM classmate;
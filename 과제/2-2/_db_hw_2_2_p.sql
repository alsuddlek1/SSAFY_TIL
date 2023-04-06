CREATE TABLE zoo (
  name TEXT NOT NULL,
  eat TEXT NOT NULL,
  weight INT NOT NULL,
  height INT,
  age INT
);

-- 1) 
--  table 순서 맞추기
INSERT INTO zoo VALUES 
('gorilla', 'omnivore',180, 210, 5);

DELETE FROM zoo WHERE rowid=3;

-- 2)
-- rowid 중복 = > 중복값 제거
SELECT rowid, * FROM zoo;

INSERT INTO zoo (rowid, name, eat, weight, age) VALUES
(3,'dolphin', 'carnivore', 210, 3),
(4, 'alligator', 'carnivore', 250, 50);

-- 3)
-- weight null => weight에 값 넣어주면됨
INSERT INTO zoo (name, eat, weight, age) VALUES
('dolphin', 'carnivore', 60, 3);

SELECT rowid, * FROM zoo;
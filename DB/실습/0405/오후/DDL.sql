-- table 만들기
CREATE TABLE contacts(
name TEXT NOT NULL,
age INTEGER NOT NULL,
email TEXT NOT NULL UNIQUE
);

-- 테이블 이름 변경
ALTER TABLE contacts RENAME TO new_contacts;

-- 테이블 열 이름 변경
ALTER TABLE new_contacts RENAME COLUMN name TO last_name;

-- 테이블열 추가 : 이때 'DERAULT'no address' 추가 해줘야댐 이유는 ppt ~~
ALTER TABLE new_contacts ADD COLUMN address TEXT NOT NULL DEFAULT'no address';

-- 데이터열 삭제 # 터미널창에서해야됨
ALTER TABLE new_contacts DROP COLUMN address;

-- table 전체 삭제
DROP TABLE new_contacts;

-- create
CREATE TABLE Worker (
  Worker_id int not null primary key ,
  first_name text,
  last_name text,
  salary integer,
  joining_date text,
  department text
);  

-- insert
INSERT INTO Worker VALUES (0001, 'Monika', 'Arora',100000,'14-02-20 09.00.00','HR');
INSERT INTO Worker VALUES (0002, 'Niharika', 'Verma',80000,'14-06-11 09.00.00','Admin');
INSERT INTO Worker VALUES (0003, 'Vishal', 'Singhal',300000,'14-02-20 09.00.00','HR');
INSERT INTO Worker VALUES (0004, 'Amitabh', 'Singh',500000,'14-02-20 09.00.00','Admin');
INSERT INTO Worker VALUES (0005, 'Vivek', 'Bhati',500000,'14-06-11 09.00.00','Admin');
INSERT INTO Worker VALUES (0006, 'Vipul', 'Diwan',200000,'14-06-11 09.00.00','Account');
INSERT INTO Worker VALUES (0007, 'Satish', 'Kumar',750000,'14-01-20 09.00.00','Account');
INSERT INTO Worker VALUES (0008, 'Geetika', 'Chauhan',90000,'14-04-1 09.00.00','Admin');


-- fetch 
 

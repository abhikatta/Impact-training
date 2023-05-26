
-- create
CREATE TABLE EMPLOYEE (
  empId INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  dept TEXT NOT NULL,
  salary INTEGER NOT NULL
);

-- insert
INSERT INTO EMPLOYEE VALUES (0001, 'Clark', 'Sales',10000);
INSERT INTO EMPLOYEE VALUES (0002, 'Dave', 'Accounting',12000);
INSERT INTO EMPLOYEE VALUES (0003, 'Ava', 'Sales',15000);
INSERT INTO EMPLOYEE VALUES (0004, 'Dave', 'Accounting',10000);
INSERT INTO EMPLOYEE VALUES (0005, 'Ava', 'Sales',132123);
INSERT INTO EMPLOYEE VALUES (0006, 'Dave', 'Accounting',294829);
INSERT INTO EMPLOYEE VALUES (0007, 'Ava', 'Sales',204892);
INSERT INTO EMPLOYEE VALUES (0008, 'Dave', 'Accounting',90000);
INSERT INTO EMPLOYEE VALUES (0009, 'Ava', 'Sales',104929);
INSERT INTO EMPLOYEE VALUES (00010, 'Dave', 'Accounting',19342874);
INSERT INTO EMPLOYEE VALUES (00011, 'Avao', 'Sales',4928112);
INSERT INTO EMPLOYEE VALUES (00012, 'Avaa', 'Tester',10000);
-- fetch 
SELECT * FROM EMPLOYEE;
delete from EMPLOYEE WHERE empId='00010';
SELECT * FROM EMPLOYEE;
SELECT * FROM EMPLOYEE order by name;
-- select empId  from EMPLOYEE group by dept;
SELECT dept, ARRAY_AGG(empid) AS empid_list FROM employee GROUP BY dept;
SELECT * FROM employee order by dept desc;

-- alter table EMPLOYEE add salary INTEGER;
-- INSERT INTO EMPLOYEE(salary) VALUES (10000);

SELECT * from EMPLOYEE;

SELECT * from EMPLOYEE WHERE name like '%a';

select name,salary from EMPLOYEE where name like '%a' group by name,salary;

select salary from EMPLOYEE where salary>5000 group by salary having count(salary)=2;

update EMPLOYEE set salary=20000 where salary=10000 and name!='Avaa';

select * from EMPLOYEE;

delete salary from EMPLOYEE where empid=1;

select * from EMPLOYEE;

INSERT into EMPLOYEE VALUES ();



-- TRIVIAL DEPENDENCIES:
-- A->B
-- A=Determinant
-- B=Dependent
-- A->B is trivial if B is a subset of A
-- 
-- 6 rules

-- 1.Inference Rule(IR):
-- 

-- create
CREATE TABLE EMPLOYEE (
  empId INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  dept TEXT NOT NULL,
  salary INTEGER NOT NULL
);

-- insert
INSERT INTO EMPLOYEE VALUES (0001, 'Clark', 'Sales',10000);
INSERT INTO EMPLOYEE VALUES (0002, 'Dave', 'Accounting',12000);
INSERT INTO EMPLOYEE VALUES (0003, 'Ava', 'Sales',15000);
INSERT INTO EMPLOYEE VALUES (0004, 'Dave', 'Accounting',10000);
INSERT INTO EMPLOYEE VALUES (0005, 'Ava', 'Sales',130000);
INSERT INTO EMPLOYEE VALUES (0006, 'Dave', 'Accounting',90000);
INSERT INTO EMPLOYEE VALUES (0007, 'Ava', 'Sales',20000);
INSERT INTO EMPLOYEE VALUES (0008, 'Dave', 'Accounting',90000);
INSERT INTO EMPLOYEE VALUES (0009, 'Ava', 'Sales',43000);
INSERT INTO EMPLOYEE VALUES (00010, 'Dave', 'Accounting',10000);
INSERT INTO EMPLOYEE VALUES (00011, 'Ava', 'Sales',1200000);

select max(salary) over(partition by dept order by empId desc)from EMPLOYEE;
select e.*,rank() over(partition by dept order by salary desc) as Ranku from EMPLOYEE e;
select e.*,dense_rank() over(partition by dept order by salary desc) as Dense_ranku from EMPLOYEE e;
select * from(
select e.*,rank() over(partition by dept order by salary desc
) as ranku from EMPLOYEE e;
)x where x.ranku<2;

WITH lowsalary AS (
  SELECT name
  FROM EMPLOYEE
  WHERE salary <10000
)
SELECT EmployeeName
FROM lowsalary;
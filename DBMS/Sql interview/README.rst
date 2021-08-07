
.. contents::
   :local:
   :depth: 3


CREATE TABLE - Count the Number of Rows
===============================================================================

.. code:: SQL

      CREATE TABLE geeks(
          id int(20) , 
          name varchar(200));

      INSERT INTO geeks(id,name) values(1,'nikhil');
      INSERT INTO geeks(id,name) values(2,'kartik');

      SELECT COUNT(id) as id_count FROM geeks

SQL query to find second highest salary?
===============================================================================

.. code:: SQL

    select FirstName, max(Salary) from employees
    where Salary not in (select max(Salary) from employees)
    
    or
    
    select FirstName, max(Salary) from employees 
    where Salary < (select max(Salary) from employees)

SQL query to find Nth highest salary?
===============================================================================

.. code:: SQL

      SELECT name, salary 
      FROM #Employee e1 
      WHERE N-1 = (SELECT COUNT(DISTINCT salary) FROM #Employee e2 
      WHERE e2.salary > e1.salary)


SQL Query to Find the Highest Salary of Each Department
===============================================================================

`Geeks <https://www.geeksforgeeks.org/sql-query-to-find-the-highest-salary-of-each-department/>`_

.. code:: SQL

      SELECT DEPT_ID, MAX(SALARY) FROM department GROUP BY DEPT_ID;

How to get the alternate rows or records from table in sql server
===============================================================================

.. code:: SQL

      select ID, NAME from department where mod(ID, 2) = 0;

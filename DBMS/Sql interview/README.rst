
.. contents::
   :local:
   :depth: 3


SQL query to find second highest salary?
===============================================================================

.. code:: SQL

    select FirstName, max(Salary) from employees
    where Salary not in (select max(Salary) from employees)
    
    or
    
    select FirstName, max(Salary) from employees 
    where Salary < (select max(Salary) from employees)


SQL Query to Find the Highest Salary of Each Department
===============================================================================

`Geeks <https://www.geeksforgeeks.org/sql-query-to-find-the-highest-salary-of-each-department/>`_

.. code:: SQL

      SELECT DEPT_ID, MAX(SALARY) FROM department GROUP BY DEPT_ID;

How to get the alternate rows or records from table in sql server
===============================================================================

.. code:: SQL

      select ID, NAME from department where mod(ID, 2) = 0;

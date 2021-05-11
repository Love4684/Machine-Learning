
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
.. code:: SQL

      SELECT DEPT_ID, MAX(SALARY) FROM department GROUP BY DEPT_ID;

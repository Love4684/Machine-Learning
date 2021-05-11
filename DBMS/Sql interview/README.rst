
.. contents::
   :local:
   :depth: 3


SQL query to find second highest salary?
===============================================================================

.. code:: c++

    select FirstName, max(Salary) from employees
    where Salary not in (select max(Salary) from employees)
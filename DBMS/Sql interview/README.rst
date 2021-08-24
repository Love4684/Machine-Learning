
.. contents::
   :local:
   :depth: 3

Key
===============================================================================

Primary key: The Primary key is an attribute in a table that can uniquely identify each record in a table. It is compulsory for every table.

Candidate key: The Candidate key is an attribute or set of an attribute which can uniquely identify a tuple. The Primary key can be selected from these attributes.

Super key: The Super key is a set of attributes which can uniquely identify a tuple. Super key is a superset of the candidate key.

Foreign key: The Foreign key is a primary key from one table, which has a relationship with another table. It acts as a cross-reference between tables.


B-Tree
===============================================================================

Following is an example of B-Tree of minimum order 5.

.. image:: https://github.com/Love4684/Machine-Learning/blob/master/DBMS/media/output253.png

 
The B+ tree is a balanced binary search tree. It follows a multi-level index format

Transaction property
===============================================================================

The transaction has the four properties. These are used to maintain consistency in a database, before and after the transaction.

Atomicity : It states that all operations of the transaction take place at once if not, the transaction is aborted.

Consistency : The integrity constraints are maintained so that the database is consistent before and after the transaction.

Isolation : It shows that the data which is used at the time of execution of a transaction cannot be used by the second transaction until the first one is completed.

Durability : The durability property is used to indicate the performance of the database's consistent state. It states that the transaction made the permanent changes.

Normalization
===============================================================================

Normalization is the process of minimizing redundancy from a relation or set of relations.
Redundancy in relation may cause insertion, deletion and updation anomalies. So, it helps to minimize the redundancy in relations.

.. code:: SQL


      1NF	A relation is in 1NF if it contains an atomic value.
      2NF	A relation will be in 2NF if it is in 1NF and all non-key attributes are fully functional dependent on the primary key.
      3NF	A relation will be in 3NF if it is in 2NF and no transition dependency exists.
      4NF	A relation will be in 4NF if it is in Boyce Codd normal form and has no multi-valued dependency.
      5NF	A relation is in 5NF if it is in 4NF and not contains any join dependency and joining should be lossless.


DELETE
===============================================================================

The DELETE statement is used to delete existing records in a table.

.. code:: SQL

   DELETE FROM Customers WHERE CustomerName='Alfreds Futterkiste'; 
   
GROUP BY
===============================================================================

The GROUP BY statement groups rows that have the same values into summary rows, like "find the number of customers in each country".

.. code:: SQL

      SELECT COUNT(CustomerID), Country
      FROM Customers
      GROUP BY Country;
      
HAVING
===============================================================================      

The HAVING clause was added to SQL because the WHERE keyword cannot be used with aggregate functions.

.. code:: SQL

      SELECT COUNT(CustomerID), Country
      FROM Customers
      GROUP BY Country
      HAVING COUNT(CustomerID) > 5;
   

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

# Write your MySQL query statement below
select e2.Name as Employee
from Employee e1, Employee e2
where e1.Id = e2.ManagerId 
and e2.Salary > e1.Salary
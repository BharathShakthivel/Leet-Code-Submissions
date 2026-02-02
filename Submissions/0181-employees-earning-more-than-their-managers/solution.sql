# Write your MySQL query statement below
SELECT T1.name as Employee
FROM Employee T1, Employee T2
WHERE T1.managerID = T2.ID
AND T1.salary > T2.salary

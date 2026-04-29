# Write your MySQL query statement below
SELECT W2.id FROM Weather W1 JOIN Weather W2 on DATEDIFF(W1.recordDate,W2.recordDate) =-1
WHERE W2.temperature > W1.temperature

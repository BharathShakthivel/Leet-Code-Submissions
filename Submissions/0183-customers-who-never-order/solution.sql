# Write your MySQL query statement below
#Using Not in (Sub Query)
-- SELECT name as Customers
-- FROM Customers
-- WHERE Customers.id NOT IN (SELECT customerId FROM Orders)

#Using LEFT JOIN
SELECT name as Customers
FROM Customers
LEFT JOIN Orders ON Customers.id = Orders.customerId
WHERE Orders.customerID IS NULL


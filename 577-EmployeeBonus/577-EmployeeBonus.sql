-- Last updated: 9/4/2025, 1:28:32 AM
# Write your MySQL query statement below

SELECT 
    name, 
    bonus
FROM Employee e
LEFT JOIN Bonus b
    ON e.empID = b.empID
WHERE bonus < 1000 OR bonus IS NULL;

-- Last updated: 8/30/2025, 11:37:08 PM
# Write your MySQL query statement below

SELECT unique_id, name
FROM Employees e
LEFT JOIN EmployeeUNI eu
    ON e.id = eu.id;
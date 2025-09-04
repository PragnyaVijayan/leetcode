-- Last updated: 9/4/2025, 1:28:29 AM
# Write your MySQL query statement below


SELECT *
FROM Cinema
WHERE description NOT LIKE '%boring%' AND id%2=1
ORDER BY rating DESC;
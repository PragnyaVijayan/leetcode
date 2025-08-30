-- Last updated: 8/29/2025, 10:43:36 PM
# Write your MySQL query statement below

SELECT name
FROM Customer
WHERE referee_id != 2 OR referee_id IS NULL;
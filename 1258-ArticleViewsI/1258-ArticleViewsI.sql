-- Last updated: 8/29/2025, 10:43:29 PM
# Write your MySQL query statement below

SELECT DISTINCT author_id AS id
FROM Views
WHERE author_id = viewer_id
ORDER BY id ASC;

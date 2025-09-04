-- Last updated: 9/4/2025, 1:28:21 AM
# Write your MySQL query statement below

SELECT customer_id, COUNT(visit_id) AS count_no_trans
FROM 
    (SELECT 
        v.visit_id,
        t.transaction_id,
        v.customer_id
    FROM Visits v
    LEFT JOIN Transactions t
        ON v.visit_id = t.visit_id) AS visitation_transaction
WHERE transaction_id IS NULL
GROUP BY customer_id;
-- Last updated: 8/29/2025, 10:43:25 PM
# Write your MySQL query statement below

SELECT tweet_id
FROM Tweets
WHERE LENGTH(content) > 15;
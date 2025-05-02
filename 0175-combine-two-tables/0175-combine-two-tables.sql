# Write your MySQL query statement below
SELECT firstName, lastName, city, state
FROM person LEFT JOIN address USING (personID)
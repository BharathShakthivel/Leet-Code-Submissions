# Write your MySQL query statement below
-- Source - https://stackoverflow.com/q/18390574
-- Posted by Fearghal, modified by community. See post 'Timeline' for change history
-- Retrieved 2026-03-03, License - CC BY-SA 4.0

WITH CTE AS (
    SELECT id,
           ROW_NUMBER() OVER (PARTITION BY email ORDER BY id) AS RowNum
    FROM person
)
DELETE FROM person
WHERE id IN (
    SELECT id
    FROM CTE
    WHERE RowNum > 1
);


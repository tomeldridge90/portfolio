/*
-----<<<<<QUESTION>>>>>-----

Write a SELECT query which will return all prime numbers smaller than 100 in ascending order.

Your query should return one column named prime.


-----<<<<<ANSWER>>>>>-----
*/ 


WITH checker AS
(
  SELECT divisor
  FROM generate_series(1,100) divisor
),
numbers AS
(
  SELECT num
  FROM generate_series(2,100) num
),
flagged AS
(
SELECT *, 
mod(num,divisor), 
CASE WHEN MOD(num,divisor) = 0 THEN 1 ELSE 0 END AS flag
FROM numbers
JOIN checker on divisor <= num
)

SELECT num AS prime
FROM flagged
GROUP BY num
HAVING SUM(flag)=2
ORDER BY num ASC
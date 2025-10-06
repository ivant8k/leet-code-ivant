-- Write your PostgreSQL query statement below
SELECT p.product_name, s.year, s.price
FROM Product p
LEFT JOIN Sales s ON s.product_id = p.product_id
WHERE year IS NOT NULL
ORDER BY year;
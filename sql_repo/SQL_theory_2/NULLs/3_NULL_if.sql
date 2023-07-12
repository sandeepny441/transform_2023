-- Handling divisions by zero
-- This will replace any zero revenue values with NULL to exclude them from reports.
SELECT NULLIF(10, 10)-- Returns NULL


--Comparing values for equality
-- You can use NULLIF to filter out join rows where two columns have the same value.
SELECT NULLIF(revenue, 0) FROM sales

-- Excluding default values
-- This will replace any rows with default status 'ACTIVE' to NULL.
SELECT NULLIF(status, 'ACTIVE') FROM accounts


-- Handling divisions by zero
-- NULLIF will return NULL instead of failing on divide by zero errors.
SELECT NULLIF(denominator,0) 
FROM calculations


-- Nulling out blanks or duplicates
-- This will turn blank values to NULL. You can also use it to null out duplicate values in a column.
SELECT NULLIF(TRIM(col),'') FROM data

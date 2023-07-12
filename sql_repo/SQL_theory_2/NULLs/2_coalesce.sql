SELECT COALESCE(NULL, NULL, 5, NULL) -- Returns 5


-- Replace NULLs with a default 'N/A' value.
SELECT 
  COALESCE(null_column, 'N/A') AS filled_column
FROM table


-- Return first non-NULL choice from a set of options.
SELECT
  COALESCE(first_choice, second_choice, third_choice)
FROM table

-- Create a new column using first non-NULL value.
SELECT
  COALESCE(col1, col2, col3) AS calculated_column
FROM table


-- Concatenate first and last name handling NULLs.
SELECT 
  COALESCE(first_name, '') || ' ' || COALESCE(last_name, '') as full_name
FROM table


-- Use default if passed value is NULL.
INSERT INTO table (column) 
VALUES (COALESCE(@value, default_value))
CREATE OR REPLACE VIEW active_fulltime_employees AS
SELECT department_id, COUNT(*) AS total
FROM employee_employee
WHERE status = 'ACTIVE' AND employment_type = 'FT'
GROUP BY department_id;

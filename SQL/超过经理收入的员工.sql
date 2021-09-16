# 1 best
SELECT
    a.Name AS 'Employee'
FROM
    Employee AS a,
    Employee AS b
WHERE
    a.ManagerId = b.Id
        AND a.Salary > b.Salary
;
# 2
SELECT Name AS Employee
FROM Employee e1
WHERE Salary > (
    SELECT Salary
    FROM Employee e2
    WHERE e1.ManagerId = e2.Id
)
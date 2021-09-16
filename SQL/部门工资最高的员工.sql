# Write your MySQL query statement below
SELECT Department.Name AS Department, 
    Employee.Name AS Employee, 
    Salary
FROM Employee, Department
WHERE DepartmentId = Department.Id AND 
    (Employee.DepartmentId , Salary) IN
    (   SELECT
            DepartmentId, MAX(Salary)
        FROM
            Employee
        GROUP BY DepartmentId
	)
;
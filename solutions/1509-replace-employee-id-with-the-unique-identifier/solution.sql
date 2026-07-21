SELECT 
    UniqueIds.unique_id, 
    Employees.name
FROM 
    Employees
LEFT JOIN 
    EmployeeUNI AS UniqueIds 
    ON Employees.id = UniqueIds.id;



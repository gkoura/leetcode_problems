import pandas as pd 
def employees_earning_more_than_managers(employee: pd.DataFrame) -> pd.DataFrame:
    # Self-join the Employee table to get manager's salary
    merged = pd.merge(employee, employee, left_on='managerId', right_on='id', suffixes=('_emp', '_mgr'))
    
    # Filter employees who earn more than their managers
    result = merged[merged['salary_emp'] > merged['salary_mgr']]
    
    # Select only the employee names
    result = result[['name_emp']].rename(columns={'name_emp': 'Employee'})
    
    return result

"""
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| salary      | int     |
| managerId   | int     |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the ID of an employee, their name, salary, and the ID of their manager.
 

Write a solution to find the employees who earn more than their managers.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Employee table:
+----+-------+--------+-----------+
| id | name  | salary | managerId |
+----+-------+--------+-----------+
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | Null      |
| 4  | Max   | 90000  | Null      |
+----+-------+--------+-----------+
Output: 
+----------+
| Employee |
+----------+
| Joe      |
+----------+
Explanation: Joe is the only employee who earns more than his manager.
"""
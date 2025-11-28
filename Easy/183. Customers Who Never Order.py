import pandas as pd
def customers_who_never_order(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # Perform a left join between Customers and Orders on customer ID
    merged = pd.merge(customers, orders, left_on='id', right_on='customerId', how='left', indicator=True)
    
    # Filter customers who have no matching orders
    no_orders = merged[merged['_merge'] == 'left_only']
    
    # Select only the customer names and rename the column
    result = no_orders[['name']].rename(columns={'name': 'Customers'})
    
    return result


"""
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the ID and name of a customer.
 

Table: Orders

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| customerId  | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
customerId is a foreign key (reference columns) of the ID from the Customers table.
Each row of this table indicates the ID of an order and the ID of the customer who ordered it.
 

Write a solution to find all customers who never order anything.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Customers table:
+----+-------+
| id | name  |
+----+-------+
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |
+----+-------+
Orders table:
+----+------------+
| id | customerId |
+----+------------+
| 1  | 3          |
| 2  | 1          |
+----+------------+
Output: 
+-----------+
| Customers |
+-----------+
| Henry     |
| Max       |
+-----------+
"""
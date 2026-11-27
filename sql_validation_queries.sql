-- Dashboard reconciliation queries (adapt table name to your SQL database)
-- 1. Total sales
SELECT SUM(Quantity * UnitPrice) AS ExpectedTotalSales
FROM Orders;

-- 2. Distinct order count
SELECT COUNT(DISTINCT OrderID) AS ExpectedDistinctOrders
FROM Orders;

-- 3. Sales by city
SELECT City, SUM(Quantity * UnitPrice) AS ExpectedSales
FROM Orders
GROUP BY City
ORDER BY City;

-- 4. Sales by category
SELECT Category, SUM(Quantity * UnitPrice) AS ExpectedSales
FROM Orders
GROUP BY Category
ORDER BY Category;

-- 5. Duplicate order IDs
SELECT OrderID, COUNT(*) AS RecordCount
FROM Orders
GROUP BY OrderID
HAVING COUNT(*) > 1;

-- 6. Required-field and quantity checks
SELECT *
FROM Orders
WHERE OrderID IS NULL
   OR OrderDate IS NULL
   OR City IS NULL
   OR Quantity <= 0
   OR UnitPrice < 0;

-- 7. Unexpected statuses
SELECT DISTINCT Status
FROM Orders
WHERE Status NOT IN ('Delivered', 'Shipped', 'Cancelled', 'Returned');

CREATE DATABASE RestaurantDB;
GO

USE RestaurantDB;

-- Bảng Menu
CREATE TABLE Menu (
    ItemID INT IDENTITY(1,1) PRIMARY KEY,
    ItemName NVARCHAR(100),
    Price INT
);

-- Bảng Orders
CREATE TABLE Orders (
    OrderID INT IDENTITY(1,1) PRIMARY KEY,
    OrderTime DATETIME DEFAULT GETDATE(),
    Status NVARCHAR(50)
);

-- Bảng OrderItems
CREATE TABLE OrderItems (
    OrderItemID INT IDENTITY(1,1) PRIMARY KEY,
    OrderID INT FOREIGN KEY REFERENCES Orders(OrderID),
    ItemID INT FOREIGN KEY REFERENCES Menu(ItemID),
    Quantity INT DEFAULT 1
);

-- Bảng hóa đơn
CREATE TABLE Invoices (
    InvoiceID INT IDENTITY(1,1) PRIMARY KEY,
    OrderID INT FOREIGN KEY REFERENCES Orders(OrderID),
    Amount INT,
    Method NVARCHAR(20)
);

-- Bảng nhân sự
CREATE TABLE Staff (
    StaffID INT IDENTITY(1,1) PRIMARY KEY,
    StaffName NVARCHAR(50),
    Role NVARCHAR(20)
);

INSERT INTO Menu (ItemName, Price)
VALUES 
('Pho', 40000),
('Fried Rice', 45000),
('Milk Tea', 30000);

INSERT INTO Staff (StaffName, Role)
VALUES
('Alice', 'waiter'),
('Bob', 'chef'),
('Carol', 'cashier'),
('David', 'manager');

CREATE TABLE Employees(
    EmployeeID INT,
    LastName VARCHAR(255),
    FirstName VARCHAR(255),
    StoreNum INT
); CREATE TABLE Locations(
    StoreNum INT,
    StoreAddress VARCHAR(255),
    StorePhone INT,
    StoreManager VARCHAR(255)
); CREATE TABLE OnlineStock(
    ProductType VARCHAR(255),
    TotalStock INT,
    AveragePrice FLOAT,
    DaysSinceSale INT
); INSERT INTO Employees(
    EmployeeID,
    LastName,
    FirstName,
    StoreNum
)
VALUES(1, 'Smith', 'Adam', 1),(2, 'Adams', 'Steve', 1),(3, 'Moir', 'Nick', 2),(4, 'Madden', 'Will', 3),(5, 'Richson', 'Kyle', 4),(6, 'Bigsby', 'Nate', 5);
INSERT INTO Locations(
    StoreNum,
    StoreAddress,
    StorePhone,
    StoreManager
)
VALUES(
    1,
    '123 Data Science Lane',
    7032091530,
    'Adam Smith'
),(
    2,
    '345 Computer Science Lane',
    7032094393,
    'Nick Moir'
),(
    3,
    '678 Computer Engineering Way',
    8001234567,
    'Will Madden'
),(
    4,
    '304 14th St NW',
    8772411234,
    'Kyle Richson'
),(
    5,
    '171 Madison Lane',
    1834192200,
    'Nate Bigsby'
);
INSERT INTO OnlineStock(
    ProductType,
    TotalStock,
    AveragePrice,
    DaysSinceSale
)
VALUES('Comics', 45, 21.63, 5),(
    'BaseballCards',
    650,
    86.42,
    1
),(
    'FootballCards',
    860,
    108.12,
    1
),(
    'BasketballCards',
    341,
    12.86,
    2
),('Collectables', 210, 240.68, 3);
SELECT
    FirstName,
    LastName
FROM
    Employees
WHERE
    StoreNum = 1;
SELECT
    TotalStock,
    AveragePrice
FROM
    OnlineStock
WHERE
    DaysSinceSale <= 2;
SELECT
    StoreAddress,
    StorePhone
FROM
    Locations;
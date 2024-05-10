BEGIN;

CREATE TABLE customer (
	"Customer_ID" INT PRIMARY KEY,
	"Age" INT,
	"Gender" VARCHAR(50),
	"Item Purchased" VARCHAR(50),
	"Category" VARCHAR(50),
	"Purchase Amount (USD)" INT,
	"Location" VARCHAR(100),
	"Size" VARCHAR(50),
	"Color" VARCHAR(50),
	"Season" VARCHAR(50),
	"Review Rating" FLOAT,
	"Subscription Status" VARCHAR(50),
	"Shipping Type" VARCHAR(50),
	"Discount Applied" VARCHAR(50),
	"Promo Code Used" VARCHAR(50),
	"Previous Purchases" INT,
	"Payment Method" VARCHAR(50),
	"Frequency of Purchases" VARCHAR(50),
	"Date" DATE
);

COMMIT;

BEGIN;

COPY customer
FROM '/files/shopping_behavior_with_dummy_month.csv' -- lokasi file CSV dalam container PostgreSQL di docker
DELIMITER ','
CSV HEADER;

COMMIT;



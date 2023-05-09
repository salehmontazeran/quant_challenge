CREATE TABLE stock_prices (
    datetime TIMESTAMP,
    close DECIMAL(10,2),
    high DECIMAL(10,2),
    low DECIMAL(10,2),
    open DECIMAL(10,2),
    volume INTEGER,
    instrument TEXT
);
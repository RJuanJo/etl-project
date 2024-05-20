use project3;
CREATE TABLE DimLocalization (
    localization_id INT AUTO_INCREMENT PRIMARY KEY,
    city VARCHAR(100)
);

CREATE TABLE DimCharacteristics (
    characteristics_id INT AUTO_INCREMENT PRIMARY KEY,
    stars FLOAT,
    name VARCHAR(255),
    guests FLOAT,
    openness FLOAT,
    hot_tub FLOAT,
    pool FLOAT,
    bedrooms FLOAT,
    bathrooms FLOAT,
    occupancy FLOAT,
    length_stay FLOAT,
    revenue FLOAT
);
CREATE TABLE DimRoomHost (
    room_host_id INT AUTO_INCREMENT PRIMARY KEY,
    roomType VARCHAR(100),
    host_type VARCHAR(100)
);
CREATE TABLE DimTimePrice (
    time_price_id INT AUTO_INCREMENT PRIMARY KEY,
    month VARCHAR(50),
    nightly_rate FLOAT
);
CREATE TABLE FactBooking (
    booking_id INT AUTO_INCREMENT PRIMARY KEY,
    localization_id INT,
    characteristics_id INT,
    room_host_id INT,
    time_price_id INT,
    lead_time FLOAT,
    FOREIGN KEY (localization_id) REFERENCES DimLocalization(localization_id),
    FOREIGN KEY (characteristics_id) REFERENCES DimCharacteristics(characteristics_id),
    FOREIGN KEY (room_host_id) REFERENCES DimRoomHost(room_host_id),
    FOREIGN KEY (time_price_id) REFERENCES DimTimePrice(time_price_id)
);
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(120) NOT NULL,
  email VARCHAR(150) UNIQUE NOT NULL,
  password VARCHAR(255) NOT NULL,
  phone VARCHAR(20),
  role VARCHAR(20) NOT NULL CHECK (role IN ('customer', 'beautician', 'admin')),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE beauticians (
  id SERIAL PRIMARY KEY,
  user_id INTEGER UNIQUE NOT NULL REFERENCES users(id),
  experience INTEGER DEFAULT 0,
  certifications TEXT,
  location VARCHAR(255),
  rating NUMERIC(2,1) DEFAULT 0.0,
  is_verified BOOLEAN DEFAULT FALSE
);

CREATE TABLE services (
  id SERIAL PRIMARY KEY,
  beautician_id INTEGER NOT NULL REFERENCES beauticians(id),
  service_name VARCHAR(120) NOT NULL,
  price NUMERIC(10,2) NOT NULL,
  duration INTEGER NOT NULL
);

CREATE TABLE bookings (
  id SERIAL PRIMARY KEY,
  customer_id INTEGER NOT NULL REFERENCES users(id),
  beautician_id INTEGER NOT NULL REFERENCES beauticians(id),
  service_id INTEGER NOT NULL REFERENCES services(id),
  date DATE NOT NULL,
  time TIME NOT NULL,
  status VARCHAR(20) DEFAULT 'pending',
  payment_status VARCHAR(20) DEFAULT 'pending'
);

CREATE TABLE reviews (
  id SERIAL PRIMARY KEY,
  customer_id INTEGER NOT NULL REFERENCES users(id),
  beautician_id INTEGER NOT NULL REFERENCES beauticians(id),
  rating INTEGER CHECK (rating BETWEEN 1 AND 5),
  comment TEXT
);

CREATE TABLE payments (
  id SERIAL PRIMARY KEY,
  booking_id INTEGER NOT NULL REFERENCES bookings(id),
  amount NUMERIC(10,2) NOT NULL,
  payment_method VARCHAR(50),
  status VARCHAR(20),
  razorpay_order_id VARCHAR(120)
);

CREATE INDEX idx_beauticians_location ON beauticians(location);
CREATE INDEX idx_services_price ON services(price);
CREATE INDEX idx_bookings_date ON bookings(date);

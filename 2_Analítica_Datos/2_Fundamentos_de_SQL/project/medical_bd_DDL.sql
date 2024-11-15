---------------------------------------
--Creación de una base de datos con DDL
---------------------------------------

CREATE DATABASE medical_db;


--------------------------------------
--Creación de las tablas de nuestra DB
--------------------------------------

--tabla pacientes
CREATE TABLE patients(
	ID BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
	name TEXT NOT NULL,
	adress VARCHAR(40),
	phone VARCHAR(30),
	date_of_birth DATE
);

--tabla médicos
CREATE TABLE physicians(
	ID INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
	name TEXT NOT NULL,
	specialty TEXT,
	licence_number TEXT UNIQUE
);

--tabla citas
CREATE TABLE appointments(
	ID BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
	patient_id BIGINT REFERENCES patients (ID),
	physician_id BIGINT REFERENCES physicians (ID),
	appointment_datetime TIMESTAMP WITH TIME ZONE
);

--tabla tratamientos
CREATE TABLE treatments(
	ID BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
	appointment_id BIGINT REFERENCES appointments (ID),
	description TEXT,
	duration INT
);

--tabla prescripciones
CREATE TABLE prescriptions(
	ID BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
	treatment_id BIGINT REFERENCES treatments (ID),
	medication_name TEXT NOT NULL,
	dosage TEXT,
	frequency TEXT
);

--tabla aseguradoras
CREATE TABLE insurance_companies(
	ID BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
	name VARCHAR(50) NOT NULL,
	contact_number VARCHAR(50),
	adress TEXT
);

--tabla hospitales
CREATE TABLE hospitals(
	ID BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
	name VARCHAR(40) NOT NULL,
	location TEXT,
	contact_number VARCHAR(50)
);

----------------------------------
--Edición de un campo en una tabla
----------------------------------

--agregamos la columna insurance_id a patients
ALTER TABLE patients
ADD COLUMN insurance_id BIGINT REFERENCES insurance_companies(ID);

--agregamos la columna gender a patients e email
ALTER TABLE patients
ADD COLUMN gender VARCHAR(10);

ALTER TABLE patients
ADD COLUMN email TEXT;

--agregamos la columna hospital_id a physicians
ALTER TABLE physicians
ADD COLUMN hospital_id BIGINT REFERENCES hospitals(ID);

--corregimos el nombre de la columna adress de insurance companies y patients
ALTER TABLE insurance_companies
RENAME COLUMN adress TO address;

ALTER TABLE patients
RENAME COLUMN adress TO address;


----------------------------------------
--Eliminación de relaciones entre tablas
----------------------------------------

--intentamos eliminar una relacion
ALTER TABLE insurance_companies
DROP COLUMN ID;

--identificamos el nombre de las restricciones para despues eliminarlas
SELECT
    constraint_name
FROM
    information_schema.key_column_usage
WHERE
    table_name = 'hospitals'
    AND column_name = 'id';

	
--eliminamos las relaciones de la base de datos
ALTER TABLE insurance_companies
DROP CONSTRAINT insurance_companies_pkey CASCADE;

ALTER TABLE appointments
DROP CONSTRAINT appointments_pkey CASCADE;

ALTER TABLE hospitals
DROP CONSTRAINT hospitals_pkey CASCADE;

ALTER TABLE patients
DROP CONSTRAINT patients_pkey CASCADE;

ALTER TABLE physicians
DROP CONSTRAINT physicians_pkey CASCADE;

ALTER TABLE prescriptions
DROP CONSTRAINT prescriptions_pkey CASCADE;

ALTER TABLE treatments
DROP CONSTRAINT treatments_pkey CASCADE;


-----------------------------------------------------------------------------------
--Eliminación del atributo IDENTITY y generacion de un serial no unico en identidad
-----------------------------------------------------------------------------------

--eliminamos ela tributo IDENTITY  de todas las tablas
ALTER TABLE insurance_companies
ALTER COLUMN id DROP IDENTITY;

ALTER TABLE appointments
ALTER COLUMN id DROP IDENTITY;

ALTER TABLE hospitals
ALTER COLUMN id DROP IDENTITY;

ALTER TABLE patients
ALTER COLUMN id DROP IDENTITY;

ALTER TABLE physicians
ALTER COLUMN id DROP IDENTITY;

ALTER TABLE prescriptions
ALTER COLUMN id DROP IDENTITY;

ALTER TABLE treatments
ALTER COLUMN id DROP IDENTITY;

--generamos una serie la cual nos va a servir para 
--incrementar automaticamente los IDs 

CREATE SEQUENCE id_serial_1
START WITH 1
INCREMENT BY 1;

CREATE SEQUENCE id_serial_2
START WITH 1
INCREMENT BY 1;

CREATE SEQUENCE id_serial_3
START WITH 1
INCREMENT BY 1;

CREATE SEQUENCE id_serial_4
START WITH 1
INCREMENT BY 1;

CREATE SEQUENCE id_serial_5
START WITH 1
INCREMENT BY 1;

CREATE SEQUENCE id_serial_6
START WITH 1
INCREMENT BY 1;

CREATE SEQUENCE id_serial_7
START WITH 1
INCREMENT BY 1;


--asignamos la serie del identificador a cada columna
--ID de nuestras tablas

ALTER TABLE insurance_companies
ALTER COLUMN id SET DEFAULT nextval('id_serial_1');

ALTER TABLE appointments
ALTER COLUMN id SET DEFAULT nextval('id_serial_2');

ALTER TABLE hospitals
ALTER COLUMN id SET DEFAULT nextval('id_serial_3');

ALTER TABLE patients
ALTER COLUMN id SET DEFAULT nextval('id_serial');

ALTER TABLE physicians
ALTER COLUMN id SET DEFAULT nextval('id_serial_4');

ALTER TABLE prescriptions
ALTER COLUMN id SET DEFAULT nextval('id_serial_5');

ALTER TABLE treatments
ALTER COLUMN id SET DEFAULT nextval('id_serial_6');

--nos aseguramos de que primary key sea el ID en cada tabla
ALTER TABLE insurance_companies
ADD CONSTRAINT insurance_companies_pkey PRIMARY KEY (id);

ALTER TABLE appointments
ADD CONSTRAINT appointments_pkey PRIMARY KEY (id);

ALTER TABLE hospitals
ADD CONSTRAINT hospitals_pkey PRIMARY KEY (id);

ALTER TABLE patients
ADD CONSTRAINT patients_pkey PRIMARY KEY (id);

ALTER TABLE physicians
ADD CONSTRAINT physicians_pkey PRIMARY KEY (id);

ALTER TABLE prescriptions
ADD CONSTRAINT prescriptions_pkey PRIMARY KEY (id);

ALTER TABLE treatments
ADD CONSTRAINT treatments_pkey PRIMARY KEY (id);
    
-------------------------------------------------------------------
--Eliminación de los datos de las tablas incorrectamente ingresados
-------------------------------------------------------------------

TRUNCATE TABLE insurance_companies RESTART IDENTITY CASCADE;
TRUNCATE TABLE appointments RESTART IDENTITY CASCADE;
TRUNCATE TABLE hospitals RESTART IDENTITY CASCADE;
TRUNCATE TABLE patients RESTART IDENTITY CASCADE;
TRUNCATE TABLE physicians RESTART IDENTITY CASCADE;
TRUNCATE TABLE prescriptions RESTART IDENTITY CASCADE;
TRUNCATE TABLE treatments RESTART IDENTITY CASCADE;

-----------------------------------------------
--Agregamos  las relaciones de la base de datos
-----------------------------------------------

--nos aseguramos de eliminar cualqueir restriccion sobre el foregein key
ALTER TABLE patients
DROP CONSTRAINT IF EXISTS patients_insurance_id_fkey;

ALTER TABLE physicians
DROP CONSTRAINT IF EXISTS physicians_hospital_id_fkey;

ALTER TABLE appointments
DROP CONSTRAINT IF EXISTS appointments_patient_id_fkey;

ALTER TABLE appointments
DROP CONSTRAINT IF EXISTS appointments_physician_id_fkey;

ALTER TABLE treatments
DROP CONSTRAINT IF EXISTS treatments_appointment_id_fkey;

ALTER TABLE prescriptions
DROP CONSTRAINT IF EXISTS prescriptions_treatment_id_fkey;


-- recreamos las relaciones entre los primary y foregein keys
ALTER TABLE patients
ADD CONSTRAINT patients_insurance_id_fkey FOREIGN KEY (insurance_id) REFERENCES insurance_companies (id);

ALTER TABLE physicians
ADD CONSTRAINT physicians_hospital_id_fkey FOREIGN KEY (hospital_id) REFERENCES hospitals (id);

ALTER TABLE appointments
ADD CONSTRAINT appointments_patient_id_fkey FOREIGN KEY (patient_id) REFERENCES patients (id);

ALTER TABLE appointments
ADD CONSTRAINT appointments_physician_id_fkey FOREIGN KEY (physician_id) REFERENCES physicians (id);

ALTER TABLE treatments
ADD CONSTRAINT treatments_appointment_id_fkey FOREIGN KEY (appointment_id) REFERENCES appointments (id);

ALTER TABLE prescriptions
ADD CONSTRAINT prescriptions_treatment_id_fkey FOREIGN KEY (treatment_id) REFERENCES treatments (id);
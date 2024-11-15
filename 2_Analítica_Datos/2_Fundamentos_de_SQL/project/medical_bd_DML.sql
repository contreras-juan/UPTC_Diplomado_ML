----------------------------------
--Actualización de valores con DML
----------------------------------

--actualizaremos los numeros de contacto de los hospitales
UPDATE hospitals
SET contact_number = '321456'
WHERE id = 1;

UPDATE hospitals
SET contact_number = '840597'
WHERE id = 2;

UPDATE hospitals
SET contact_number = '410236'
WHERE id = 3;

UPDATE hospitals
SET contact_number = '785124'
WHERE id = 4;

UPDATE hospitals
SET contact_number = '102030'
WHERE id = 5;

UPDATE hospitals
SET contact_number = '645122'
WHERE id = 6;

UPDATE hospitals
SET contact_number = '302015'
WHERE id = 7;

UPDATE hospitals
SET contact_number = '251436'
WHERE id = 8;

UPDATE hospitals
SET contact_number = '132022'
WHERE id = 9;

------------------------------------------
--Consulta de valores unicos en las tablas
------------------------------------------

SELECT DISTINCT name
FROM  patients;

SELECT DISTINCT name
FROM hospitals;

SELECT DISTINCT address
FROM insurance_companies;

SELECT DISTINCT medication_name
FROM prescriptions;

-----------------------------------------
--Consultas básicas mediante proyecciones
-----------------------------------------

--selección de columnas específicas
SELECT name, id, gender, insurance_id
FROM patients;

--seleccion de columnas específicas condicionadas
SELECT name, id, gender, insurance_id, email
FROM patients
WHERE date_of_birth > '22-04-2024';

SELECT name, id, gender
FROM patients
WHERE insurance_id = 1;

--consulta de valores textuales con respecto a un patron
SELECT p.id, p.name, p.date_of_birth
FROM patients p
WHERE p.name LIKE 'A%'
ORDER BY p.name ASC
LIMIT 5;

--consulta mediante múltiples condiciones y conversión de tipo
SELECT treatment_id, medication_name, dosage
FROM prescriptions
WHERE (dosage > 1 and dosage < 3) and (frequency > 50);

SELECT treatment_id, medication_name, dosage, frequency
FROM prescriptions
WHERE 
	(CAST(dosage AS NUMERIC) > 1.0 AND CAST(dosage AS NUMERIC) < 3.0) AND 
	(CAST(frequency AS NUMERIC) > 1 AND CAST(frequency AS NUMERIC) < 5);
 
 
--selección y creación de columnas inplace en consultas
SELECT 
	name, 
	date_of_birth, 
	gender, email,
	EXTRACT(year from AGE(CURRENT_DATE, date_of_birth)) AS age
FROM patients
--WHERE age = 30; 
WHERE EXTRACT(YEAR FROM AGE(CURRENT_DATE, date_of_birth)) = 30;

--selección de datos de acuerdo a un intervalo de fechas
SELECT *
FROM appointments
WHERE appointment_datetime BETWEEN '2024-01-01' AND '2024-12-31';

--ordenamiento de tablas por campo especifico
SELECT *
FROM treatments
ORDER BY duration DESC;

SELECT *
FROM prescriptions
ORDER BY dosage DESC;

---------------------------------------------------
--Consultas básicas mediante proyecciones agrupadas
---------------------------------------------------

--agrupacion por columna sencilla
SELECT gender, COUNT(*) as cuenta_genero
FROM patients
GROUP BY gender
ORDER BY cuenta_genero DESC;

--promedio de una agrupacion
SELECT medication_name, ROUND( AVG(CAST(dosage AS NUMERIC)) ,3) AS dosage_promedio
FROM prescriptions
GROUP BY medication_name
ORDER BY dosage_promedio DESC;

--promedio de agrupación filtrado previamente
SELECT medication_name, ROUND( AVG(CAST(dosage AS NUMERIC)) ,3) AS dosage_promedio
FROM prescriptions
WHERE (CAST(dosage AS NUMERIC)) > 3
GROUP BY medication_name
ORDER BY dosage_promedio DESC;

--promedio de agrupación, con filtrado posterior a la agrupacion
SELECT medication_name, ROUND( AVG(CAST(dosage AS NUMERIC)) ,3) AS dosage_promedio
FROM prescriptions
WHERE (CAST(dosage AS NUMERIC)) > 1
GROUP BY medication_name
HAVING AVG((CAST(dosage AS NUMERIC))) > 3
ORDER BY dosage_promedio DESC;


-------------------------------
--Consultas con uniones básicas
-------------------------------

--left joins
SELECT p.name, p.gender, p.email, i.name, i.contact_number
FROM patients AS p
LEFT JOIN insurance_companies AS i ON p.insurance_id = i.id;

SELECT p.name, p.specialty, h.name, h.contact_number
FROM physicians AS p
LEFT JOIN hospitals AS h ON p.hospital_id = h.id;

SELECT p.name, p.gender, p.email, a.physician_id, a.appointment_datetime
FROM patients AS p
LEFT JOIN appointments AS a ON p.id = a.patient_id;

--right joins
SELECT p.name, p.gender, p.email, i.name AS insurance_name, i.contact_number
FROM patients AS p
RIGHT JOIN insurance_companies AS i ON p.insurance_id = i.id;

SELECT p.name, p.specialty, h.name AS hospital_name, h.contact_number
FROM physicians AS p
RIGHT JOIN hospitals AS h ON p.hospital_id = h.id;

SELECT p.name, p.gender, p.email, a.physician_id, a.appointment_datetime
FROM patients AS p
RIGHT JOIN appointments AS a ON p.id = a.patient_id;

--inner joins
SELECT p.name, p.gender, p.email, i.name AS insurance_name, i.contact_number
FROM patients AS p
JOIN insurance_companies AS i ON p.insurance_id = i.id;

SELECT t.appointment_id, t.description, t.duration, p.medication_name, p.dosage, p.frequency
FROM treatments AS t
JOIN prescriptions AS p ON t.id = p.treatment_id
ORDER BY  p.dosage DESC;

--outer join
SELECT p.name, p.gender, p.email, i.name AS insurance_name, i.contact_number
FROM patients AS p
FULL OUTER JOIN insurance_companies AS i ON p.insurance_id = i.id;

SELECT t.appointment_id, t.description, t.duration, p.medication_name, p.dosage, p.frequency
FROM treatments AS t
FULL OUTER JOIN prescriptions AS p ON t.id = p.treatment_id
ORDER BY  p.dosage DESC;

---------------------------------
--Consultas con uniones agrupadas
---------------------------------

--numero de medicos por hospital
SELECT hospitals.name, COUNT(*) AS number_physicians
FROM hospitals
LEFT JOIN physicians
ON hospitals.id = physicians.hospital_id
GROUP BY hospitals.id

--numero de citas en las que un paciente se involucro
SELECT p.id AS patient_id, p.name,  COUNT(a.id) AS appointment_count
FROM patients p
LEFT JOIN appointments a ON p.id = a.patient_id
GROUP BY p.id, p.name
ORDER BY appointment_count DESC;

--conteo de pacientes por compañia aseguradora
SELECT ic.name AS insurance_company_name, COUNT(p.id) AS number_of_patients
FROM insurance_companies ic
JOIN patients p ON ic.id = p.insurance_id
GROUP BY ic.name
ORDER BY number_of_patients DESC;


--------------------------------
--Joins multiples o concatenados
--------------------------------

--número de tratamientos recibidos por paciente
SELECT p.name AS patient_name, COUNT(t.id) AS number_of_treatments
FROM patients p
JOIN appointments a ON p.id = a.patient_id
JOIN treatments t ON a.id = t.appointment_id
GROUP BY p.name
ORDER BY number_of_treatments DESC;

--número de pacientes diferentes atendidos por hospital
SELECT h.name AS hospital_name, COUNT(DISTINCT p.id) AS number_of_patients
FROM hospitals h
JOIN physicians ph ON h.id = ph.hospital_id
JOIN appointments a ON ph.id = a.physician_id
JOIN patients p ON a.patient_id = p.id
GROUP BY h.name
ORDER BY number_of_patients DESC;

--número de pacientes distintos atendidos por medico
SELECT ph.name AS physician_name, COUNT(DISTINCT a.patient_id) AS number_of_patients
FROM physicians ph
JOIN appointments a ON ph.id = a.physician_id
JOIN patients p ON a.patient_id = p.id
GROUP BY ph.name
ORDER BY number_of_patients DESC;

--número de tratamientos por hospital
SELECT h.name AS hospital_name, COUNT(t.id) AS number_of_treatments
FROM hospitals h
JOIN physicians ph ON h.id = ph.hospital_id
JOIN appointments a ON ph.id = a.physician_id
JOIN treatments t ON a.id = t.appointment_id
GROUP BY h.name
ORDER BY number_of_treatments DESC;

------------------------------------------
--Consultas anidadas y consultas complejas
------------------------------------------

--consulta anidada básica No correlacionada
SELECT name 
FROM patients 
WHERE id IN (SELECT patient_id 
			 FROM appointments 
			 WHERE appointment_datetime > '2024-01-01');
			 
--consulta anidada básica correlacionada
SELECT p.name
FROM patients p
WHERE EXISTS (SELECT p.name 
			  FROM appointments a 
			  WHERE a.patient_id = p.id AND a.appointment_datetime > '2023-01-01');


--dosage promedio por medicacion prescrita por cada medico, pero solo para aquellos
--medicos que han prescrito un numero específico de medicamentos
SELECT DISTINCT ph.name AS physician_name, AVG(CAST(p.dosage AS NUMERIC)) AS average_dosage
FROM physicians ph
JOIN appointments a ON ph.id = a.physician_id
JOIN treatments t ON a.id = t.appointment_id
JOIN prescriptions p ON t.id = p.treatment_id
WHERE p.dosage IS NOT NULL
GROUP BY ph.name
HAVING COUNT(p.id) > 10
ORDER BY average_dosage DESC
LIMIT 5 OFFSET 0;

--número total promedio de pacientes distintos por médico
WITH patient_counts AS (
    SELECT ph.id AS physician_id, COUNT(DISTINCT a.patient_id) AS number_of_patients
    FROM physicians ph
    JOIN appointments a ON ph.id = a.physician_id
    GROUP BY ph.id
)
SELECT AVG(number_of_patients) AS average_patients_per_physician
FROM patient_counts;

--número promedio de tratamientos por medico y especialidad de medico
SELECT specialty, AVG(treatment_count) AS average_treatments_per_specialty
FROM (
    SELECT ph.id AS physician_id, ph.specialty, COUNT(t.id) AS treatment_count
    FROM physicians ph
    JOIN appointments a ON ph.id = a.physician_id
    JOIN treatments t ON a.id = t.appointment_id
    GROUP BY ph.id, ph.specialty
) AS physician_treatments
GROUP BY specialty
ORDER BY average_treatments_per_specialty DESC;


--dosage promedio por tratamiento
SELECT treatment_description, AVG(total_dosage) AS average_dosage_per_treatment
FROM (
    SELECT t.id AS treatment_id, t.description AS treatment_description, SUM(CAST(p.dosage AS NUMERIC)) AS total_dosage
    FROM treatments t
    JOIN prescriptions p ON t.id = p.treatment_id
    GROUP BY t.id, t.description
	ORDER BY t.id DESC
) AS treatment_dosages
GROUP BY treatment_description
ORDER BY average_dosage_per_treatment DESC;

--categorización de los dosage como low, medium y high
SELECT treatment_id, treatment_description,
    CASE
        WHEN total_dosage < 10 THEN 'Low'
        WHEN total_dosage BETWEEN 11 AND 20 THEN 'Medium'
        ELSE 'High'
    END AS dosage_category
FROM (
    SELECT t.id AS treatment_id, t.description AS treatment_description, SUM(CAST(p.dosage AS NUMERIC)) AS total_dosage
    FROM treatments t
    JOIN prescriptions p ON t.id = p.treatment_id
    GROUP BY t.id, t.description
) AS treatment_dosages
ORDER BY treatment_id;



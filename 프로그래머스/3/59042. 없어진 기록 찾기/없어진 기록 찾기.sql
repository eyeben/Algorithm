SELECT
    O.ANIMAL_ID,
    O.NAME    
FROM ANIMAL_OUTS O
LEFT JOIN ANIMAL_INS I USING (ANIMAL_ID)
WHERE I.ANIMAL_ID IS NULL
ORDER BY 1;
;
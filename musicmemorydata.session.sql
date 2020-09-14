INSERT INTO musicmemoryapi_likedsong
VALUES
    ('1', 'Strongly Disagree'),
    ('2', 'Disagree'),
    ('3', 'Neutral'),
    ('4', 'Agree'),
    ('5', 'Strongly Agree');



DELETE FROM musicmemoryapi_patientsong
WHERE ID = 1;

DELETE From musicmemoryapi_patient
WHERE ID = 4;

DELETE FROM musicmemoryapi_songresponse

SELECT subject_name
FROM subjects
where teacher_id IN (SELECT id from teachers where teacher_name = 'Володимир Дробаха')
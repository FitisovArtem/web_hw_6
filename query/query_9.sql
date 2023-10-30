SELECT s.subject_name
FROM subjects as s
join grade_book as gd on gd.subject_id = s.id
join students as st on st.id = gd.students_id
where st.students_name = 'пані Ірина Дараган'
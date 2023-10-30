SELECT s.subject_name
FROM subjects as s
join grade_book as gd on gd.subject_id = s.id
join students as st on st.id = gd.students_id
join teachers as t on t.id = s.teacher_id
where st.id = 9
and t.id = 1
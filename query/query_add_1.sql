SELECT t.teacher_name, st.students_name, avg(gd.grade)
FROM subjects as s
join grade_book as gd on gd.subject_id = s.id
join students as st on st.id = gd.students_id
join teachers as t on t.id = s.teacher_id
where st.id = 6
and t.id = 2
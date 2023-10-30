SELECT st.students_name, gr.group_name, s.subject_name, max(gd.date_of) as date_last_visit
FROM grade_book as gd
join students as st on st.id = gd.students_id
join groups as gr on gr.id = st.group_id
join subjects as s on s.id = gd.subject_id

where gr.id = 1
and s.id = 2
group by st.students_name
select g.group_name, ROUND(AVG(gb.grade)) as avg_grade
from grade_book as gb
join students as st on st.id = gb.students_id
join groups as g on g.id = st.group_id
where gb.subject_id = 3
group by g.group_name
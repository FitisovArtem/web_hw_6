SELECT students_name
FROM students
where id IN (select students_id
from grade_book
where subject_id = 4
group by students_id
order by avg(grade) desc limit 1)
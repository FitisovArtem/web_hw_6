SELECT students_name
FROM students
where id IN (select students_id
from grade_book
group by students_id
order by avg(grade) desc limit 5)
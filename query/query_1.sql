SELECT students_name
FROM students
where id IN (SELECT students_id from grade_book order by grade desc limit 5)
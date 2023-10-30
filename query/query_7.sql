SELECT s.students_name, gd.grade
FROM students as s
join groups as g on g.id = s.group_id
join grade_book as gd on gd.students_id = s.id
join subjects as sub on sub.id = gd.subject_id
where g.group_name = 'mollitia'
and sub.subject_name = 'sed'

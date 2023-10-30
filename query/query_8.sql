SELECT t.teacher_name, sub.subject_name, round(AVG(gd.grade)) avg_grade
FROM teachers as t
join subjects as sub on sub.teacher_id = t.id
join grade_book as gd on gd.subject_id = sub.id
where t.id = 1
group by sub.subject_name
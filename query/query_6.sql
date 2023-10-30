SELECT students_name
FROM students
where group_id IN (SELECT id from groups where group_name = 'maiores')
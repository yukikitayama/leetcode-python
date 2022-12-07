with cte as (
    select
        department_id,
        count(student_id) as num_student
    from
        students
    group by
        1
)

select
    a.student_id,
    a.department_id,
    ifnull(round((rank() over(
        partition by a.department_id
        order by a.mark desc
    ) - 1) * 100 / (b.num_student - 1), 2), 0) as percentage
from
    students as a
left join
    cte as b
on
    a.department_id = b.department_id
;

select
  case
    # Current student id is odd, and is not the number of student (that case, id needs not to be modified)
    when mod(id, 2) != 0 and id != num_student then id + 1
    when mod(id, 2) != 0 and id = num_student then id
    else id - 1
  end as id,
  student
from
  seat,
  (
select
  count(*) as num_student
from
  seat
) as a
order by
  id
;
with recursive
cte as (
  select
    task_id,
    subtasks_count as subtask_id
  from
    tasks
  union all
  select
    task_id,
    subtask_id - 1 as subtask_id
  from
    cte
  where
    subtask_id > 1
)

-- select * from cte order by 1, 2;

select
  task_id,
  subtask_id
from
  cte
where
  (task_id, subtask_id) not in (
    select * from executed
  )
;

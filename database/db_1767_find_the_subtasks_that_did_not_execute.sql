-- Generate sequence of numbers and not in subtask_id to find
with recursive cte as (
  select
    task_id,
    subtasks_count,
    1 as subtask_id
  from
    tasks

  union

  select
    task_id,
    subtasks_count,
    subtask_id + 1 as subtask_id
  from
    cte
  where
    -- Use < because subtask_id + 1 will be equal to subtask_count
    subtask_id < (
      select
        max(subtasks_count)
      from
        tasks
    )
)

select
  a.task_id,
  a.subtask_id
from
  cte as a
left join
  executed as b
on
  a.task_id = b.task_id
  and a.subtask_id = b.subtask_id
where
  b.subtask_id is null
  and a.subtasks_count >= a.subtask_id

;

-- self join?

select
  a.log_id as start_id,
  -- Becuase earlier range will contain the later continuous range
  -- For each start id, find the earliest end id to avoid overlapping ranges
  min(b.log_id) as end_id
from
  -- id whose id - 1 not existing in the table is the start id
  (
    select
      log_id
    from
      logs
    where
      log_id - 1 not in (
        select
          log_id
        from
          logs
      )
  ) as a,
  -- end id is the opposite
  (
    select
      log_id
    from
      logs
    where
      log_id + 1 not in (
        select
          log_id
        from
          logs
      )
  ) as b
-- Becuase a id needs to be always earlier than or equal to b id
-- Solve the reverse situation
where
  a.log_id <= b.log_id
group by
  a.log_id
;
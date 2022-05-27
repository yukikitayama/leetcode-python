select
  -- Without max(), null precedes real name values to show up
  max(case
    when continent = 'America' then name
  end) as america,
  max(case
    when continent = 'Asia' then name
  end) as asia,
  max(case
    when continent = 'Europe' then name
  end) as europe
from
  (
    select
      *,
      row_number() over(
        partition by continent
        order by name
      ) as row_id
    from
      student
  ) as a

group by
  row_id

;

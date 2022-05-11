select
  b.name as country
from
  person as a
inner join
  country as b
on
  substring(a.phone_number, 1, 3) = b.country_code
inner join
  calls as c
on
  a.id in (c.caller_id, c.callee_id)
group by
  b.name
having
  avg(duration) > (
    select
      avg(duration)
    from
      calls
  )
;
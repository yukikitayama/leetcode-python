(
select
  name as results
from
  movierating as a
left join
  users as b
on
  a.user_id = b.user_id
group by
  b.name
order by
  count(a.user_id) desc,
  b.name
limit
  1
)

union

(
select
  b.title as results
from
  movierating as a
left join
  movies as b
on
  a.movie_id = b.movie_id
where
  year(created_at) = 2020
  and month(created_at) = 2
group by
  b.title
order by
  avg(rating) desc,
  b.title
limit
  1
)
;
with
-- Name of user who has rating the greatest number of movies
cte1 as (
select
  a.user_id,
  b.name,
  count(a.rating) as num_rating
from
  movierating as a
left join
  users as b
on
  a.user_id = b.user_id
group by
  1
order by
  3 desc,
  2
limit
  1
),

-- Movie name with the highest average rating in 2020-02
cte2 as (
select
  a.movie_id,
  b.title,
  avg(a.rating) as avg_rating
from
  movierating as a
left join
  movies as b
on
  a.movie_id = b.movie_id
where
  left(created_at, 7) = '2020-02'
group by
  a.movie_id
order by
  3 desc,
  2
limit
  1
)

select
  name as results
from
  cte1
union
select
  title as results
from
  cte2
;

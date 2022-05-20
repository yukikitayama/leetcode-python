# Write your MySQL query statement below
select
  a.score,
  count(b.score) as 'rank'
from
  scores as a,
  (
    select
      distinct score
    from
      scores
  ) as b
where
  a.score <= b.score
group by
  a.id
order by
  a.score desc
;


# SELECT S.Score, COUNT(S2.Score) as `Rank`
# FROM Scores S,
# (SELECT DISTINCT Score FROM Scores) S2
# WHERE S.Score<=S2.Score
# GROUP BY S.Id
# ORDER BY S.Score DESC;
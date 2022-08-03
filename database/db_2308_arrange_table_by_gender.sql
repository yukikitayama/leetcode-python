select
  user_id,
  gender
from (
select
  user_id,
  gender,
  dense_rank() over(partition by gender order by user_id) as rank_in_gender,
  -- Make another rank because we wanna order gender by specifically female -> other -> male
  if(gender = 'female', 1, if(gender = 'other', 2, 3)) as rank_of_gender
from
  genders
order by
  3,
  4,
  1
) as a
;
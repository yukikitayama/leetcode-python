# Write your MySQL query statement below
# select
#   distinct page_id as recommended_page
# from
#   likes
# where
#   (
#   user_id in (
#     select
#       user2_id
#     from
#       friendship
#     where
#       user1_id = 1
#   )
#   or user_id in (
#     select
#       user1_id
#     from
#       friendship
#     where
#       user2_id = 1
#   )
#   )
#   and page_id not in (
#     select
#       page_id
#     from
#       likes
#     where
#       user_id = 1
#   )
# ;

select
  distinct b.page_id as recommended_page
from (
  select
    case
      when user1_id = 1 then user2_id
      when user2_id = 1 then user1_id
    end as user_id
  from
    friendship
) as a
inner join
  likes as b
on
  a.user_id = b.user_id
where
  page_id not in (
    select
      page_id
    from
      likes
    where
      user_id = 1
  )
;


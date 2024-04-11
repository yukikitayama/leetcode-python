/*
555.2 * 900 = 499,680

Compute sum of square footage of prime
Compute 500,000 / the sum as integer
Integre multiplied by the count of prime items is item count for prime
Compute the sum * the integer as total square for prime
Compute the difference between 500000 - the prime total square

*/

# Write your MySQL query statement below
with type_stats as (
  select
    item_type,
    sum(square_footage) as sum_square,
    count(item_category) as num_category
  from
    inventory
  group by
    1
),

prime as (
  select
    *,
    -- floor(500000 / sum_square) as combination,
    floor(500000 / sum_square) * num_category as item_count,
    500000 - (floor(500000 / sum_square) * sum_square) as room_for_not_prime
  from
    type_stats
  where
    item_type = 'prime_eligible'
),

not_prime as (
  select
    *,
    -- floor((select room_for_not_prime from prime) / sum_square) as combination,
    floor((select room_for_not_prime from prime) / sum_square) * num_category as item_count
  from
    type_stats
  where
    item_type = 'not_prime'
)

-- select * from type_stats;
-- select * from prime;
-- select * from not_prime;

select
  item_type,
  item_count
from
  prime
union all
select
  item_type,
  item_count
from
  not_prime
;

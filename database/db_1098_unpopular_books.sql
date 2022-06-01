select
  book_id,
  name
from
  books
where
  available_from < '2019-05-23'
  and book_id not in (
    select
      book_id
    from
      orders
    -- Last year
    where
      dispatch_date between '2018-06-23' and '2019-06-23'
    group by
      book_id
    having
      sum(quantity) >= 10
  )
;


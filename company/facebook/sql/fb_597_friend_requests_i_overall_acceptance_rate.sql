with cte as (
select
  count(distinct(requester_id, accepter_id)) as num_accept,
  count(distinct(sender_id, send_to_id)) as num_request
from
  friendrequest,
  requestaccepted
)

select
  case
    when num_request = 0 then 0
    else round(cast(num_accept as decimal) / cast(num_request as decimal), 2)
    -- Same as above
    -- else round(num_accept::decimal / num_request::decimal, 2)
  end accept_rate
from
  cte
;

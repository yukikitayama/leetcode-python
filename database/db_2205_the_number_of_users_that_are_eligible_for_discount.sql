create function getUserIDs(startDate date, endDate date, minAmount int) returns int
begin
  return (
  select
    count(distinct user_id) as user_cnt
  from
    purchases
  where
    amount >= minAmount
    and time_stamp between startDate and endDate
  );
end;
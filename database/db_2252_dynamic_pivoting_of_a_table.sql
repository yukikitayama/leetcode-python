CREATE PROCEDURE PivotProducts()
BEGIN
	# Write your MySQL query statement below.

    -- Override GROUP_CONCAT default length
    set session group_concat_max_len = 1000000;

    -- Dynamically generated columns statement is stored into a variable and used later
	select
      # group_concat(
      #   distinct concat(
      #     'sum(case when store = "',
      #     store,
      #     '" then price end) as ',
      #     store
      #   )
      # )
      -- Create price columns for each store
      group_concat(distinct concat('sum(case when store = "', store, '" then price end) as ', store))
    into
      @each_store_column_statement
    from
      products;

    -- select @each_store_column_statement;

    -- Create a main query
    set
      @main_query = concat('select product_id, ', @each_store_column_statement, ' from products group by product_id');

    -- Execute the main query
    -- Prepare a statement
    prepare final_query from @main_query;
    -- Execute the prepared statement
    execute final_query;
    -- Release the prepared statement
    deallocate prepare final_query;

END
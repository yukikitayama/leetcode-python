CREATE PROCEDURE UnpivotProducts()
BEGIN
	# Write your MySQL query statement below.

    set session group_concat_max_len = 1000000;

	select
      -- *
      -- table_catalog,
      -- table_schema,
      -- table_name,
      -- column_name

      -- Write query for each store
      -- Using backticks and concat allows us to insert actual names into @main_query
      -- Double quoatation for the first `column_name` intends to insert column name as string into query
      group_concat(
        concat('select product_id, "', `column_name`, '" as store, ', `column_name`, ' as price from products where ', `column_name`, ' is not null')
        separator ' union '
      )

    into @main_query

    -- Get all the store columns information from metadata table
    from
      information_schema.columns
    where
      table_schema = 'test'
      and table_name = 'products'
      and column_name != 'product_id'
    ;

    -- select @main_query;

    prepare sql_query from @main_query;
    execute sql_query;
    deallocate prepare sql_query;

END
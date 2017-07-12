

Operator	Right Operand Type	Description	Example	Example Result
->	int	Get JSON array element (indexed from zero, negative integers count from the end)	'[{"a":"foo"},{"b":"bar"},{"c":"baz"}]'::json->2	{"c":"baz"}
->	text	Get JSON object field by key	'{"a": {"b":"foo"}}'::json->'a'	{"b":"foo"}
->>	int	Get JSON array element as text	'[1,2,3]'::json->>2	3
->>	text	Get JSON object field as text	'{"a":1,"b":2}'::json->>'b'	2
#>	text[]	Get JSON object at specified path	'{"a": {"b":{"c": "foo"}}}'::json#>'{a,b}'	{"c": "foo"}
#>>	text[]	Get JSON object at specified path as text	'{"a":[1,2,3],"b":[4,5,6]}'::json#>>'{a,2}'	3





SELECT  to_timestamp(('{"foo": [true, "bar",1499785539], "tags": {"a": 1, "b": null}}'::json#>>'{foo,2}')::INT) ;

--select * from mo_data_20170524 where id ='桂F86863' and time BETWEEN  1495555200 and 1495609532
-- select count(*) from mo_data_20170527;

-- select  count(*) from  mo_data_20170528 where (last::json#>>'{data,A,provider}') = '3' limit 1;
-- select count(*) from mo_data_20170615;
-- select to_char( to_timestamp(last::json#>>'{data,A,time}'), 'HH12:MI:SS') from mo_data_20170711 where id='沪DH3368'  order by last::json#>>'{data,A,time}' desc
-- select last from mo_data_20170711 where id='沪DH3368'  order by last::json#>>'{data,A,time}' desc

-- select time,last from mo_data_20170711 where id='皖K3C691' and (time BETWEEN 1499702400 and 1499785539) order by time desc
select time,data,last from mo_data_20170712 where id='皖K3C691'  order by time desc;
-- delete from mo_data_20170711;
select id,to_timestamp(time),to_number(last::json#>>'{data,A,time}') from mo_data_20170712 where id='皖K3C691' order  by time desc;
select DISTINCT id from mo_data_20170711;

SELECT  to_timestamp(('{"foo": [true, "bar",1499785539], "tags": {"a": 1, "b": null}}'::json#>>'{foo,2}')::INT) ;

--提取json数组中的轨迹记录
select id,to_timestamp(time), to_timestamp( (last::json#>>'{data,A,time}')::int) from mo_data_20170712 where id='皖K3C691' order  by time desc;


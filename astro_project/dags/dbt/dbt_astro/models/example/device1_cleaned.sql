{{ config(materialized='table',post_hook =" update {{this}} set os_name='unknown' where os_name is null", schema ='curated') }}

--select 1 as name
-- where id is not null

SELECT distinct * FROM mock_project.public.device1



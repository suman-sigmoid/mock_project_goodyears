{{ config(materialized='table',post_hook =[
" update {{this}} set gender='unknown' where gender != 'Male' and gender !='Female' or gender is NULL ",
"update {{this}} set year_of_birth = (select avg(year_of_birth) from {{this}}) where year_of_birth is NULL "],
schema ='curated') }}

--select 1 as name
-- where id is not null

SELECT distinct * FROM mock_project.public.crm1



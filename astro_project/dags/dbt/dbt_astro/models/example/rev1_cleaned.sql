
{{ config(materialized='table', schema ='curated') }}


--select 1 as name
-- where id is not null

SELECT distinct  * FROM mock_project.public.rev1
WHERE msisdn IS NOT NULL or week_number is not null or revenue_usd is not null


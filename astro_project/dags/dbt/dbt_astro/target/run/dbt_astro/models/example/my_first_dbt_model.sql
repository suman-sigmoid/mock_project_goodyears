

      create or replace transient table mock_project.curated.my_first_dbt_model  as
      (--

--select 1 as name
-- where id is not null
CREATE TABLE CURATED.REV1_STAGED
(msisdn varchar,week_number NUMBER, revenue_usd float);

INSERT INTO rev1_staged
SELECT DISTINCT *
FROM raw.rev1
WHERE msisdn IS NOT NULL or week_number is not null or revenue_used is not null;
      );
    
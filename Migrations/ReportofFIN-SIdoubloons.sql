--
-- T_REPORT_GROUP Update
--
if (not exists (SELECT *
		FROM t_report_group
		WHERE report_group_label='FIN-SI'))
begin
	INSERT INTO t_report_group (report_group_label)
	SELECT 'FIN-SI'
end


--
-- T_DBACTIONS Update
--
DELETE FROM T_DBActions WHERE label='Report of FIN-SI doubloons'
INSERT INTO t_dbactions 
(label, command, comments,report_group_idr)
SELECT
	'Report of FIN-SI doubloons',
	'select date as [Date], time as [Time], fin_ci_sv as [FIN CI], state as [State], cause as [Cause], Interface from FIN_SI_LOADER_Report where state = ''DELETED'' or state = ''MERGED''',
	'- List of doubloons (deleted, merged)',
	report_group_id

FROM
	t_report_group
WHERE
	report_group_label='FIN-SI'


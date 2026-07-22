SELECT 
    ROUND(
        COUNT(A.player_id) / (SELECT COUNT(DISTINCT player_id) FROM Activity), 
        2
    ) AS fraction
FROM 
    (
        SELECT player_id, MIN(event_date) AS first_login
        FROM Activity
        GROUP BY player_id
    ) F
LEFT JOIN 
    Activity A 
    ON F.player_id = A.player_id 
    AND A.event_date = DATE_ADD(F.first_login, INTERVAL 1 DAY);


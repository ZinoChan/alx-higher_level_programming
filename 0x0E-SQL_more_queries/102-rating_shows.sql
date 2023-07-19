-- Lists all shows
SELECT `title`, SUM(`rate`) AS `rating`
  FROM `tv_shows` AS s
       INNER JOIN `tv_show_ratings` AS r
       ON s.`id` = r.`show_id`
 GROUP BY `title`
 ORDER BY `rating` DESC;

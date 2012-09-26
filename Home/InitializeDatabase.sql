CREATE TRIGGER HappyLinkGenAdj AFTER INSERT On Adjective AS MERGE INTO FluffyLink As HL USING (SELECT Adjective.Text + Copy.Text + Noun.Text FROM Adjective INNER JOIN Adjective AS [Copy] ON Adjective.Text != Copy.Text CROSS JOIN Nouns) AS Source(Text) ON (HL.Text) = (Source.Text) WHEN NOT MATCHED THEN INSERT (Text, LastAccessed) VALUES (Source.Text, NULL);
CREATE TRIGGER HappyLinkGenNoun AFTER INSERT On Noun AS MERGE INTO FluffyLink As HL USING (SELECT Adjective.Text + Copy.Text +  Noun.Text FROM Adjective INNER JOIN Adjective AS [Copy] ON Adjective.Text != Copy.Text CROSS JOIN Nouns) AS Source(Text) ON (HL.Text) = (Source.Text) WHEN NOT MATCHED THEN INSERT (Text, LastAccessed) VALUES (Source.Text, NULL);


SELECT
CONCAT(a.Text, c.Text, n.Text)
FROM public."Home_adjective" a
INNER JOIN public."Home_adjective" c
ON a.Text != c.Text
CROSS JOIN public."Home_noun" n;

select docid from Frequency where (term="transactions") or (term="world") group by docid having count(*) > 1;

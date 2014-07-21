select docid, sum(count) from Frequency group by docid having sum(count) > 300;

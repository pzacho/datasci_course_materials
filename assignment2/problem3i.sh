#!/bin/sh
sqlite3 reuters.db < problem3i.sql | head -n 1 > keyword_search.txt

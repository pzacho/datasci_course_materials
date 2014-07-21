#!/bin/sh
sqlite3 reuters.db < problem1a.sql | wc -l > select.txt

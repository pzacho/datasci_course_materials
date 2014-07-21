#!/bin/sh
sqlite3 reuters.db < problem1b.sql | wc -l > select_project.txt

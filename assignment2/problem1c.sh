#!/bin/sh
sqlite3 reuters.db < problem1c.sql | wc -l > union.txt

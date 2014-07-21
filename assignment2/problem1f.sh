#!/bin/sh
sqlite3 reuters.db < problem1f.sql | wc -l > two_words.txt

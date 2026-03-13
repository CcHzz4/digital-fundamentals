#!/bin/bash

df -h | awk 'NR>1 {print $1, $5; if ($5+0 > 90) print "WARNING: " $1 " is " $5 " full"}'

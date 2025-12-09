#!/bin/bash
frames=(frame_*.txt)
fps=30
delay=$(awk "BEGIN {print 1/$fps}")

while true; do
  for f in "${frames[@]}"; do
    clear
    cat "$f"
    sleep "$delay"
  done
done

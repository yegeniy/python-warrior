#!/usr/bin/env fish
set -l pwdir /Users/ew/dev/github.com/yegeniy/python-warrior
set -l warrior $pwdir/pythonwarrior/(basename (pwd))
set -l result ($pwdir/bin/pythonwarrior -d $warrior -s -t0 2>&1 | tail -n 1);
set -l score (switch '"'$result'"';
  case '*Total Score: *'; echo $result | rev | cut -d' ' -f1 | rev; 
  case '*Sorry*'; echo -1; 
  case '*Exception*'; echo -10; 
  case '*'; echo -10; end)
echo $result $score
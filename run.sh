#!/bin/bash

# pandoc -t revealjs -s $1 -o $2 --highlight-style=pygments --self-contained --slide-level=2 --standalone --smart
# pandoc -t revealjs -s $1 -o $2 --highlight-style=tango --self-contained --slide-level=2 --standalone --smart
# pandoc -t revealjs -s $1 -o $2 --highlight-style=espresso --self-contained --slide-level=2 --standalone --smart
# pandoc -t revealjs -s $1 -o $2 --highlight-style=zenburn --self-contained --slide-level=2 --standalone --smart
# pandoc -t revealjs -s $1 -o $2 --highlight-style=kate --self-contained --slide-level=2 --standalone --smart
# pandoc -t revealjs -s $1 -o $2 --highlight-style=monochrome --self-contained --slide-level=2 --standalone --smart
# pandoc -t revealjs -s $1 -o $2 --highlight-style=breezedark --self-contained --slide-level=2 --standalone --smart
# pandoc -t revealjs -s $1 -o $2 --highlight-style=haddock --self-contained --slide-level=2 --standalone --smart


# pandoc -toc -s \
#        -i \
#        --from=markdown \
#        --standalone \
#        --number-sections \
#        --to=html5 \
#        --highlight-style=kate \
#        --self-contained \
#        --slide-level=2 \
#        --resource-path=. \
#        --variable theme="black" \
#        --variable transition="linear" \
#        -t revealjs $1 \
#        --mathjax \
#        -o $2

pandoc -toc -s \
       -i \
       --from=markdown \
       --standalone \
       --number-sections \
       --highlight-style=kate \
       --self-contained \
       --slide-level=2 \
       --wrap=auto \
       --incremental \
       --columns 80 \
       --resource-path=. \
       --variable theme="Frankfurt" \
       -t beamer $1 \
       -o $2

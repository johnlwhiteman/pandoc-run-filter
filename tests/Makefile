.PHONY: clean
FLAGS        = \
  --from=markdown \
  --self-contained \
  --standalone \
  --mathml
FILTERS = \
	--filter pandoc-run-filter
ODIR=./__pandoc_run

all: 01 02 03 04 05

# Verify in="shell" out="text" as an epub
01:
	pandoc -i $@.md ${FLAGS} ${FILTERS} --metadata title=$@ --to epub3 -o ${ODIR}/$@.epub

# Verify in="shell" out="image" as an epub
02:
	pandoc -i $@.md ${FLAGS} ${FILTERS} --metadata title=$@ --to epub3 -o ${ODIR}/$@.epub

# Verify in="script" out="text" as an epub
03:
	pandoc -i $@.md ${FLAGS} ${FILTERS} --metadata title=$@ --to epub3 -o ${ODIR}/$@.epub

# Verify in="script" out="image img="venn04.png" as an epub
04:
	pandoc -i $@.md ${FLAGS} ${FILTERS} --metadata title=$@ --to epub3 -o ${ODIR}/$@.epub

# Verify in="script" out="image img="co05.png" as a pdf
05:
	pandoc -i $@.md ${FLAGS} ${FILTERS} --metadata title=$@ --to pdf -o ${ODIR}/$@.pdf

# Verify in="script" out="image img="co05.png" as a pdf
06:
	pandoc -i $@.md ${FLAGS} ${FILTERS} --metadata title=$@ --to epub -o ${ODIR}/$@.epub


clean:
	-rm -rf *.epub ${ODIR}/*

.PHONY: clean
FLAGS        = \
  --from=markdown \
  --self-contained \
  --standalone \
  --mathml \
  --toc \
  --toc-depth=2
FILTERS = \
	--filter pandoc-run-filter

01:
	pandoc -i $@.md ${FLAGS} ${FILTERS} --metadata title=$@ --to epub3 -o $@.epub

02:
	pandoc -i $@.md ${FLAGS} ${FILTERS} --metadata title=$@ --to epub3 -o $@.epub

clean:
	-rm -rf *.epub

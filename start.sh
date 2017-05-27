#! /bin/bash

rm out.txt
spark-submit \
  --master "local[2]" \
  --name "StreamPageAnalyzer" \
  --py-files "title_extractors.py,extraction_utils.py,content_extractors.py,author_extractors.py,date_extractor.py" \
   run.py \
   urls.txt \
   out.txt

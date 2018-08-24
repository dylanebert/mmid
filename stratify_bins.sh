#!/bin/bash
python scripts/stratify_bins.py -i pairs/nouns_sample -o bins/nouns_sample/
python scripts/stratify_bins.py -i pairs/verbs_sample -o bins/verbs_sample/
python scripts/stratify_bins.py -i pairs/adjectives_sample -o bins/adjectives_sample/
python scripts/stratify_bins.py -i pairs/concrete_nouns -o bins/concrete_nouns/
python scripts/stratify_bins.py -i pairs/concrete_verbs -o bins/concrete_verbs/
python scripts/stratify_bins.py -i pairs/concrete_adjectives -o bins/concrete_adjectives/
python scripts/stratify_bins.py -i pairs/abstract_nouns -o bins/abstract_nouns/
python scripts/stratify_bins.py -i pairs/abstract_verbs -o bins/abstract_verbs/
python scripts/stratify_bins.py -i pairs/abstract_adjectives -o bins/abstract_adjectives/

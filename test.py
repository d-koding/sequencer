
from bgp import ia

ia_query = 'mediatype:texts AND licenseurl:"http://creativecommons.org/licenses/by-nc/3.0/" AND isbn:*'
books = ia.search_items(ia_query)
[book for book in books]
ocaids = [b['identifier'] for b in books]
from bgp import DEFAULT_SEQUENCER
for ocaid in ocaids[0:2]:
    book = ia.get_item(f'{ocaid}')
    genome = DEFAULT_SEQUENCER.sequence(book)
    print(genome.results)
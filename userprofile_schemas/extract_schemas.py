"""Extraction of some schemas collected as examples.
"""

from .core import extract_schema_from_csvs
import prov.model as prov
import datetime

AMAZON_SAMPLES = '../samples/amazon' 
AMAZON_OUTPUT = 'schemas/amazon/amazon.sql'


def gen_prov_file():
    """Creates provenance file for the data schema. 
    """
    document = prov.ProvDocument()
    document.set_default_namespace('http://dapsi-example.org/')
    document.add_namespace('ex', 'http://dapsi-example.org/')
    e2 = document.entity('e2', (
        (prov.PROV_TYPE, "File"),
        ('ex:path', "/amazon.sql"),
        ('ex:creator', "Miguel-Angel Sicilia"),
        ('ex:content', "Amazon user profile schema"),
    ))

    a1 = document.activity('a1', datetime.datetime.now(), None, {prov.PROV_TYPE: "edit"})
    # References can be qnames or ProvRecord objects themselves
    document.wasGeneratedBy(e2, a1, None, {'ex:fct': "run_transformer"})
    document.wasAssociatedWith('a1', 'ag2', None, None, {prov.PROV_ROLE: "author"})
    document.agent('ag2', {prov.PROV_TYPE: 'prov:Person', 'ex:name': "Miguel-Angel Sicilia"})
    print(document.get_provn())

def main():
    amazon = extract_schema_from_csvs(AMAZON_SAMPLES)
    with open(AMAZON_OUTPUT) as f: f.write(amazon)
    gen_prov_file()


if __name__ == '__main__':
    main()
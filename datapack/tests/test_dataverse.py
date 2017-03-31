import datapack.dataverse as ddv

def test_metadata():
    doi = "10.7910/DVN/BSHEML"
    meta = ddv.metadata(doi)
    assert (meta['datasetVersion']['files'][0]['description'] ==
            "Picture of a cat")

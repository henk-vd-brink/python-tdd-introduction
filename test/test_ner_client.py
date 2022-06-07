import unittest

from flask_ner import NamedEntityClient
from test_doubles import NerModelTestDouble

class TestNerClient(unittest.TestCase):
    
    def test_get_ents_returns_dictionary_given_empty_string_causes_empty_spacy_doc_ents(self):
        model = NerModelTestDouble("eng")
        model.returns_doc_ents([])

        ner = NamedEntityClient(model)
        ents = ner.get_ents("")
        self.assertIsInstance(ents, dict)

    def test_get_ents_returns_dictionary_given_nonempty_string_causes_empty_spacy_doc_ents(self):
        model = NerModelTestDouble("eng")
        model.returns_doc_ents([])

        ner = NamedEntityClient(model)
        ents = ner.get_ents("Madison is a city in the Wisconsin.")
        self.assertIsInstance(ents, dict)
    
    def test_get_ents_given_spacy_PERSON_is_returned_serializes_to_Person(self):
        model = NerModelTestDouble("eng")
        doc_ents = [{"text": "Lauren Fressinet", "label_": "PERSON"}]
        model.returns_doc_ents(doc_ents)

        ner = NamedEntityClient(model)
        result = ner.get_ents("...")

        expected_result = {
            "ents": [{"ent": "Lauren Fressinet", "label": "Person"}],
            "html": "" 
        }

        self.assertListEqual(result["ents"], expected_result["ents"])

    def test_get_ents_given_spacy_PERSON_is_returned_serializes_to_Person(self):
        model = NerModelTestDouble("eng")
        doc_ents = [{"text": "Lauren Fressinet", "label_": "PERSON"}]
        model.returns_doc_ents(doc_ents)

        ner = NamedEntityClient(model)
        result = ner.get_ents("...")

        expected_result = {
            "ents": [{"ent": "Lauren Fressinet", "label": "Person"}],
            "html": "" 
        }

        self.assertListEqual(result["ents"], expected_result["ents"])

    def test_get_ents_given_spacy_NORP_is_returned_serializes_to_Group(self):
        model = NerModelTestDouble("eng")
        doc_ents = [{"text": "Lithuanian", "label_": "NORP"}]
        model.returns_doc_ents(doc_ents)

        ner = NamedEntityClient(model)
        result = ner.get_ents("...")

        expected_result = {
            "ents": [{"ent": "Lithuanian", "label": "Group"}],
            "html": "" 
        }

        self.assertListEqual(result["ents"], expected_result["ents"])

    def test_get_ents_given_spacy_LOC_is_returned_serializes_to_Location(self):
        model = NerModelTestDouble("eng")
        doc_ents = [{"text": "Eiffeltower", "label_": "LOC"}]
        model.returns_doc_ents(doc_ents)

        ner = NamedEntityClient(model)
        result = ner.get_ents("...")

        expected_result = {
            "ents": [{"ent": "Eiffeltower", "label": "Location"}],
            "html": "" 
        }

        self.assertListEqual(result["ents"], expected_result["ents"])

    def test_get_ents_given_spacy_LANGUAGE_is_returned_serializes_to_Language(self):
        model = NerModelTestDouble("eng")
        doc_ents = [{"text": "ASL", "label_": "LANGUAGE"}]
        model.returns_doc_ents(doc_ents)

        ner = NamedEntityClient(model)
        result = ner.get_ents("...")

        expected_result = {
            "ents": [{"ent": "ASL", "label": "Language"}],
            "html": "" 
        }

        self.assertListEqual(result["ents"], expected_result["ents"])
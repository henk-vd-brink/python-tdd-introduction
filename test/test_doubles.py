import typing

DocTestDouble_ = typing.NewType("DocTestDouble_", object)


class SpanTestDouble:
    """
    Test double for spacy Span
    """

    def __init__(self, text: str, label: str) -> None:
        self.text = text
        self.label_ = label


class DocTestDouble:
    """
    Test double for spacy Doc
    """

    def __init__(self, sent: str, ents: typing.List[typing.Dict[str, str]]) -> None:
        self.sent = sent
        self.ents = [SpanTestDouble(ent["text"], ent["label_"]) for ent in ents]


class NerModelTestDouble:
    """
    Test double for spacy NLP model
    """

    def __init__(self, model: str) -> None:
        self.model = model

    def returns_doc_ents(self, ents: typing.List[typing.Dict[str, str]]) -> None:
        self.ents = ents

    def __call__(self, sent: str) -> DocTestDouble:
        return DocTestDouble(sent, self.ents)

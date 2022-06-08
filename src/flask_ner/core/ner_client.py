import typing


class NamedEntityClient:
    def __init__(self, model: typing.Any) -> None:
        self.model = model

    def get_ents(self, sent: str) -> typing.Dict[str, typing.Any]:
        doc = self.model(sent)
        entities = [
            {"ent": ent.text, "label": self.map_label(ent.label_)} for ent in doc.ents
        ]
        return {"ents": entities, "html": ""}

    @staticmethod
    def map_label(label: str) -> typing.Union[str, None]:
        label_map = {
            "PERSON": "Person",
            "NORP": "Group",
            "LOC": "Location",
            "LANGUAGE": "Language",
        }
        return label_map.get(label)

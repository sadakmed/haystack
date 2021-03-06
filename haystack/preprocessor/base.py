from typing import List, Dict, Any, Optional

from haystack import BaseComponent


class BasePreProcessor(BaseComponent):
    outgoing_edges = 1

    def process(
        self,
        document: dict,
        clean_whitespace: Optional[bool] = True,
        clean_header_footer: Optional[bool] = False,
        clean_empty_lines: Optional[bool] = True,
        split_by: Optional[str] = "word",
        split_length: Optional[int] = 1000,
        split_overlap: Optional[int] = None,
        split_respect_sentence_boundary: Optional[bool] = True,
    ) -> List[dict]:
        """
        Perform document cleaning and splitting. Takes a single document as input and returns a list of documents.
        """
        raise NotImplementedError

    def clean(
        self, document: dict, clean_whitespace: bool, clean_header_footer: bool, clean_empty_lines: bool,
    ) -> Dict[str, Any]:
        raise NotImplementedError

    def split(
        self,
        document: dict,
        split_by: str,
        split_length: int,
        split_overlap: int,
        split_respect_sentence_boundary: bool,
    ) -> List[Dict[str, Any]]:
        raise NotImplementedError

    def run(self, document: dict, **kwargs): # type: ignore
        documents = self.process(document)

        result = {"documents": documents, **kwargs}
        return result, "output_1"

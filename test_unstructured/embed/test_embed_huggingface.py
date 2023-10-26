from unstructured.documents.elements import Text
from unstructured.embed.huggingface import HuggingFaceEmbeddingEncoder


def test_embed_documents_does_not_break_element_to_dict(mocker):
    # Mocked client with the desired behavior for embed_documents
    mock_client = mocker.MagicMock()
    mock_client.embed_documents.return_value = [1, 2]

    # Mock get_openai_client to return our mock_client
    mocker.patch.object(
        HuggingFaceEmbeddingEncoder,
        "get_huggingface_client",
        return_value=mock_client,
    )

    encoder = HuggingFaceEmbeddingEncoder()
    elements = encoder.embed_documents(
        elements=[Text("This is sentence 1"), Text("This is sentence 2")],
    )
    assert len(elements) == 2
    assert elements[0].to_dict()["text"] == "This is sentence 1"
    assert elements[1].to_dict()["text"] == "This is sentence 2"
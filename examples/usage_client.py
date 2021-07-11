import sys

sys.path.append("../muse_as_service")

from muse_as_service import MUSEClient  # noqa: E402

# params
ip = "localhost"
port = 5000

# init client
client = MUSEClient(ip=ip, port=port)

# login
client.login(username="admin", password="admin")

# sentences
sentences = ["This is sentence example.", "This is yet another sentence example."]

# tokenizer
tokenized_sentence = client.tokenize(sentences)

# embedder
embedding = client.embed(sentences)

# logout
client.logout()

# results
print(tokenized_sentence)  # [
# ["▁This", "▁is", "▁sentence", "▁example", "."],
# ["▁This", "▁is", "▁yet", "▁another", "▁sentence", "▁example", "."]
# ]
print(embedding.shape)  # (2, 512)


# tests
import numpy as np  # noqa: E402

np.testing.assert_equal(
    tokenized_sentence,
    [
        ["▁This", "▁is", "▁sentence", "▁example", "."],
        ["▁This", "▁is", "▁yet", "▁another", "▁sentence", "▁example", "."],
    ],
)
np.testing.assert_equal(
    embedding.shape,
    (2, 512),
)

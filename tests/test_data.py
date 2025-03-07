from src.data.text.preprocessing import preprocess_text

def test_preprocessing():
    text = "A Sci-Fi movie with spaceships!"
    expected = ['scifi', 'movie', 'spaceship']
    assert preprocess_text(text) == expected
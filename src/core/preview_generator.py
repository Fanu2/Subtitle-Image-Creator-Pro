class PreviewGenerator:
    """Generates preview text."""

    SAMPLE_TEXT = (
        "This is a sample subtitle.\n"
        "The real subtitle preview\n"
        "will appear here."
    )

    def generate(self) -> str:
        """Return preview text."""

        return self.SAMPLE_TEXT
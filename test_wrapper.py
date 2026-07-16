from src.core.text_wrapper import TextWrapper

wrapper = TextWrapper()

text = (
    "This is a very long subtitle that should automatically wrap "
    "onto multiple lines exactly like a professional subtitle."
)

print(wrapper.wrap(text))
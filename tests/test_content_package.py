from packages.llm.content_package import generate_content_package
from packages.llm.save_package import save_content_package

news = {
    "title": "OpenAI meluncurkan model AI terbaru yang lebih cepat dan murah.",
    "source": "Reuters",
    "link": "https://example.com"
}

package = generate_content_package(news)

print("PACKAGE GENERATED")

filepath = save_content_package(package)

print("FILE SAVED TO:")
print(filepath)
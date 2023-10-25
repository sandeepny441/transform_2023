from transformers import pipeline

summarizer = pipeline("summarization", model="t5-small", tokenizer="t5-small")


# # Load the fine-tuned GPT-2 model
# summarizer = pipeline("summarization", model="your_fine_tuned_model", tokenizer="gpt2")

# Your text
text = """
A transformer is a passive component that transfers electrical energy from one electrical circuit to another circuit, or multiple circuits. A varying current in any coil of the transformer produces a varying magnetic flux in the transformer's core, which induces a varying electromotive force (EMF) across any other coils wound around the same core. Electrical energy can be transferred between separate coils without a metallic (conductive) connection between the two circuits. Faraday's law of induction, discovered in 1831, describes the induced voltage effect in any coil due to a changing magnetic flux encircled by the coil.
"""

# Generate the summary
summary = summarizer(text, max_length=50, min_length=25, do_sample=False)
print(summary[0]['summary_text'])

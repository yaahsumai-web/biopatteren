from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

BIO_KNOWLEDGE = [
    {
        "keywords": ["dna", "டிஎன்ஏ"],
        "answer": (
            "DNA (deoxyribonucleic acid) stores hereditary information. "
            "It uses four bases: A, T, G, and C."
        ),
    },
    {
        "keywords": ["gc content", "gc"],
        "answer": (
            "GC content is the percentage of G and C bases in a DNA sequence. "
            "It describes a sequence but cannot identify an organism by itself."
        ),
    },
    {
        "keywords": ["blast"],
        "answer": (
            "BLAST is an NCBI sequence-comparison tool. It compares a DNA or "
            "protein sequence against database records to find similar sequences."
        ),
    },
    {
        "keywords": ["ncbi", "database", "databases"],
        "answer": (
            "NCBI provides nucleotide sequences, genomes, literature, and BLAST. "
            "For protein records, UniProt is also a trusted database."
        ),
    },
    {
        "keywords": ["protein", "uniprot"],
        "answer": (
            "UniProt is a protein database containing protein sequences, "
            "function annotations, and evidence links."
        ),
    },
    {
        "keywords": ["genome", "genomics"],
        "answer": (
            "A genome is the complete DNA content of an organism. "
            "Genomics studies genomes, genes, and genetic variation."
        ),
    },
    {
        "keywords": ["alignment", "sequence analysis"],
        "answer": (
            "Sequence alignment compares DNA, RNA, or protein sequences to "
            "find similar regions, differences, and possible relationships."
        ),
    },
]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/chat", methods=["POST"])
def chatbot():
    data = request.get_json(silent=True) or {}

    question = data.get("message", "").strip().lower()

    if not question:
        return jsonify({
            "reply": "Please enter a bioinformatics question."
        }), 400

    for topic in BIO_KNOWLEDGE:
        if any(word in question for word in topic["keywords"]):
            return jsonify({
                "reply": topic["answer"]
            })

    return jsonify({
        "reply": (
            "I am BioPattern, a bioinformatics learning assistant. "
            "Please ask about DNA, GC content, BLAST, genomes, sequence "
            "alignment, NCBI, UniProt, or biological databases."
        )
    })


if __name__ == "__main__":
    app.run(debug=True)
from dotenv import load_dotenv
from utils.audio_processor import process_input
from core.transcriber import transcribe_all
from core.summarizer import summarize, generate_title
from core.extractor import extract_all
from core.rag_engine import build_rag_chain, ask_question

load_dotenv()

def run_pipeline(source : str, language :str = "english") -> dict:
    print("starting AI video Asistant")

    # Step 1: Process input
    chunks = process_input(source)

    # Step 2: Transcribe audio
    transcript = transcribe_all(chunks, language)
    print(f"raw transscription (first 300 characters ) {transcript[:300]}")

    # Step 3: Generate title
    title = generate_title(transcript)

    # Step 4: Generate summary
    summary = summarize(transcript)

    # Step 5: Extract action items, decisions and questions
    extracted_data = extract_all(transcript)

    # Step 6: Build RAG chain
    rag_chain = build_rag_chain(transcript)

    return {
        "title": title,
        "transcript": transcript,
        "summary": summary,
        "extracted_data": extracted_data,
        "rag_chain": rag_chain,
    }


if __name__ == "__main__":
    # Phase 1: CLI entry point
    source = input("Enter YouTube URL or local file path: ").strip()
    language = input("Language (english/hinglish): ").strip() or "english"
    result = run_pipeline(source, language)

    print("\n" + "=" * 60)
    print(f"📌 Title: {result['title']}")
    print(f"\n📋 Summary:\n{result['summary']}")
    # print(f"\nAction Items:\n{result['action_items']}")
    # print(f"\nKey Decisions:\n{result['key_decisions']}")
    # print(f"\nOpen Questions:\n{result['open_questions']}")
    print(f"\n✅ Meeting Analysis:\n{result['extracted_data']}")
    print("=" * 60)

    # Phase 2: Chat with your meeting via RAG
    print("\nChat with your meeting (type 'exit' to quit)\n")
    rag_chain = result["rag_chain"]

    while True:
        question = input("You: ").strip()

        if question.lower() in ["exit", "quit", "q"]:
            print("Goodbye!")
            break

        if not question:
            continue

        try:
            answer = ask_question(rag_chain, question)
            print(f"\nAssistant: {answer}\n")
        except Exception as e:
            print(f"\nAPI Error: {e}")
            print("Please try again after some time.\n")
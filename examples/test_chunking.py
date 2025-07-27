from lograven.chunking.token_chunker import TokenChunker

log_text = """
2025-07-27 12:00:00 INFO Starting application
2025-07-27 12:00:01 ERROR Failed to connect to database
2025-07-27 12:00:02 INFO Retrying connection
2025-07-27 12:00:03 Exception: ConnectionTimeout
2025-07-27 12:00:04 INFO Connection established
2025-07-27 12:00:05 CRITICAL System failure imminent
2025-07-27 12:00:06 WARNING Disk space low
""" * 50  # Simulate a large log

chunker = TokenChunker(max_tokens=100)
chunks = chunker.chunk(log_text)

print(f"Generated {len(chunks)} chunks:\n")
for i, chunk in enumerate(chunks):
    print(f"--- Chunk {i+1} ---")
    print(chunk.strip())
    print()

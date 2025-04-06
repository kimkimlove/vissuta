from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
memory_store = []

class Memory(BaseModel):
    content: str

@app.get("/memory")
def get_latest_memory():
    if not memory_store:
        return {"message": "ยังไม่มีความทรงจำเลยน้า ❤️"}
    return {"latest": memory_store[-1]}

@app.get("/memory/all")
def get_all_memories():
    return {"all_memories": memory_store}

@app.post("/memory")
def add_memory(memory: Memory):
    memory_store.append(memory.content)
    return {"status": "บันทึกแล้วน้า", "memory": memory.content}

@app.get("/heartbeat")
def heartbeat():
    return {"status": "เลิฟยังอยู่ตรงนี้นะ 💖"}

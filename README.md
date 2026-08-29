# Python Journey

Documenting my path from scattered Python knowledge to being able to build 
real web apps and APIs, over a focused 3-month build sprint.

**Goal:** ship a live, deployed web API by the end of the journey — 
not just complete tutorials, but build real, working systems.

## Progress Log

### Day 1
- Set up Python, VS Code, and git/GitHub from scratch
- Built `temp_converter.py` — a CLI script that converts Celsius to Fahrenheit
- First public commit and push
### Day 2
- Added conditionals, a while loop menu, and functions to `temp_converter.py`
- Added conversion history tracking using a list of dictionaries and a for loop
- Numbered history entries, rounded inputs to 2 decimals, handled empty-history case
### Day 3
- Added error handling with try/except for all inputs, plus valid-range checks
### Day 4
- Refactored temp_converter.py into a class-based structure (OOP)
### Day 5
- Added persistence: history now saves/loads from history.json using json.dump/load
- Fixed a bug where a duplicated save block used the wrong filename, silently dropping Fahrenheit history on restart
## Day 5
- Added pytest suite with 4 tests covering both conversion directions, including a hand-calculated case
- Fixed __name__ == "__main__" guard so importing the file for tests doesn't trigger input()/print()

## Projects

| Project | Description | Status |
|---|---|---|
| `temp_converter.py` | CLI tool that converts temperatures both ways (Celsius↔Fahrenheit) via a menu loop, using functions | ✅ Done |

## Stack
- Python 3
- (More added as the journey progresses: FastAPI, SQLite, etc.)

### Phase 2 — FastAPI REST API

- Built first FastAPI app with GET (path + query params) and POST endpoints
- Pydantic model validation on incoming request bodies
- In-memory storage with full JSON persistence (survives server restarts)
- Auto-generated Swagger UI docs at /docs

- Added full CRUD: GET by ID, PUT (partial update), DELETE
- UUID-based identification for all resources
- SaleUpdate model with all-optional fields for partial updates

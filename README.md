echo "# facebook_agent" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Nkm17000/facebook_agent.git
git push -u origin main



***********************************
# Facebook Agent

Simple FastAPI project.

## Run

```bash
pip install -r requirements.txt

for powershell : python -m uvicorn app.main:app --reload
uvicorn app.main:app --reload
```

Open

http://127.0.0.1:8000

Swagger

http://127.0.0.1:8000/docs
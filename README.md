# FitBot
FitBOt is a multi-agent system that jhelps users with sports injuries and nutrition

## Data
The data source for this application is vertex AI datastores. The config for this datatstores is as follows:
parser: layout
enabled table and image annotations
chunk size: 200 tokens with ancestral headings

2 different vertex search apps are setup for injuries and nutrition having their respective datastores

# Agent Development iterations
testing single agent on server

curl -X POST http://localhost:8000/apps/agents/users/test/sessions/test \
  -H "Content-Type: application/json" \
  -d '{"state": {"key1": "value1", "key2": 42}}'

curl -X POST http://localhost:8000/run \
-H "Content-Type: application/json" \
-d '{
"appName": "agents",
"userId": "test",
"sessionId": "test",
"newMessage": {
    "role": "user",
    "parts": [{
    "text": "Hello"
    }]
}
}'
# 🏃🏻‍♂️FitBot🏋️‍♀️

**FitBot** is a multi-agent Sports Doctor built to assist athletes and fitness enthusiasts with injury management and nutrition planning. The system is powered by two intelligent agents: one focused on injuries and the other on nutrition. It also integrates with a **Vertex AI Search Agent** (deployed via Vertex AI Agent Builder) to extract knowledge from uploaded PDF documents, enabling contextual and dynamic responses based on domain-specific resources.

---

## Access the Application
The application can be accessed [here](https://sports-doctor-137358858062.europe-west2.run.app)

## 🚀 Key Features

- 🧠 **Multi-agent architecture** for modular specialization:
  - **Injury Agent**: Diagnoses and offers recovery suggestions.
  - **Nutrition Agent**: Offers dietary recommendations based on athletic needs.
- 🔍 **Vertex AI Search Agent** integration for document-driven knowledge.
- ☁️ Easily deployable to Google Cloud using custom scripts.

---

## 🧠 Vertex AI Integration
This project utilizes Google Cloud’s Vertex AI Agent Builder as a knowledge base for:

1. Ingesting and parsing PDF documents as knowledge sources.
2. Enabling agents to answer queries with context-aware accuracy.
3. You can manage the knowledge base and deploy agents via the Vertex AI Agent Builder console.

### Steps taken to create the knowledge base:

1. **Collection**: Collect documents (preferrably PDFs) to beb used as knwledge sources for sports nutrition and injuries
2. **Upload**:  Create 2 separate GCS buckets and upload the documents as per their domain into these buckets
3. **Vetrex AI Search App**: Create 2 Vertex AI Search applications, each having one GCS datastore created using the GCS buckets

## 🗂️ Repository Structure
<pre>
.
├── LICENSE 
├── README.md 
├── microservices  
│   ├── backend -----------------------------> has the complete backend code written usinfADK framework 
│   │   ├── cr_deployment.sh ----------------> the script to deploy the agent to a cloud run service 
│   │   └── src 
│   │       ├── __init__.py 
│   │       ├── agent.py --------------------> the main parent agent 
│   │       ├── config.py -------------------> constants definition 
│   │       ├── helper_agents ---------------> helper agents for nutrition and injury advice 
│   │       │   ├── injury_agent.py 
│   │       │   └── nutrition_agent.py 
│   │       ├── prompts ---------------------> has all the prompts and agent descriptions used by different agents 
│   │       │   ├── big_doc.py 
│   │       │   ├── injury_agent.py 
│   │       │   └── nutrition_agent.py 
│   │       ├── requirements.txt ------------> has all the python modules required to run the agents 
│   │       ├── tools -----------------------> contains all the tools used by all the agents 
│   │       │   ├── injury_tool.py 
│   │       │   └── nutrition_tool.py 
│   │       └── utils -----------------------> any utility function being used by the agents 
│   │           └── datastore_helper.py -----> function to query the vertex AI search apps with references 
│   └── frontend ----------------------------> currently empty as we are using the built in ADK UI 
└── tests -----------------------------------> currently empty 
</pre>

---

## 🧑‍💻 Getting Started
### 0. Requirements
📦 Requirements
Before you begin, ensure your environment meets the following requirements:

#### 🖥️ System Requirements
- Python 3.12+
- pip (Python package manager)
- Virtual environment support (venv or virtualenv)
- Google Cloud SDK (for deploying to Vertex AI & Cloud Run)

#### ☁️ Google Cloud Platform (GCP)
- A GCP project with:
- Vertex AI Agent Builder enabled
- Cloud Run enabled
- Vertex AI Search setup with a document store (PDF knowledge base)
- Proper IAM roles for deploying and accessing Vertex AI agents:
  - Vertex AI Agent User
  - Cloud Run Admin
  - Service Account Token User
  - Vertex AI Search Admin

### 1. Clone the Repository

```bash
git clone [https://github.com/your-org/fitbot.git](https://github.com/Hardikr23/FitBot.git)
cd fitbot
```

### Setup
```bash
cd microservices/backend/src
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Test Locally
We can run the solution locally by running:
```bash
adk web
```
This command will give a localhost link where we can test the solution via a UI
More ways of testing the solution locally can be found [here](https://google.github.io/adk-docs/get-started/testing/)

### Deployment (Cloud Run)
Ensure you are authenticated to GCP and the cloud  build service account has the right permissions to deployy to cloud run.
The permission can be granted using the below command:
```bash
gcloud projects add-iam-policy-binding $GOOGLE_CLOUD_PROJECT \
  --member="serviceAccount:${PROJECT_NUMBER}@cloudbuild.gserviceaccount.com" \
  --role="roles/iam.serviceAccountUser"
```

To deploy the application navigate to the <code>backend</code> folder and run:
```bash
./cr_deployment.sh
```
other options for deployment like Agent Engine or custom UI can be found [here](https://google.github.io/adk-docs/deploy/)

## 📄 License
This project is licensed under the MIT License.

## 🙋‍♀️ Contributing
We welcome contributions! Please open issues or submit PRs for bugs, enhancements, or documentation improvements.

## 📬 Contact
For questions or collaborations, feel free to reach out via GitHub Issues or email [hardikr68@gmail.com](mailto:hardikr68@gmail.com)

Peace out! ✌🏼